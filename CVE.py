import os
import copy
import sys
from CVE_DB import *
from CVE_EXTRA import *

CVE_EXTRA_KNOWN = [k[0] for k in CVE_DB_EXTRA]
blacklist = ["prima","wlan","qcacld","sock_setsockopt","bcmdhd","flounder","fix CVE-2016-8474","mediatek"]
cve_blacklist = ["CVE-2014-9880",
"CVE-2014-9904",
"CVE-2015-8830",
"CVE-2016-3859",
"CVE-2016-3893",
"CVE-2016-7914",
"CVE-2017-0435",
"CVE-2017-0436",
"CVE-2017-0583",
"CVE-2017-0636",
"CVE-2017-0650",
"CVE-2017-0750",
"CVE-2017-6247",
"CVE-2017-8264",
"CVE-2017-10663",
"CVE-2012-6701",
"CVE-2014-9872",
"CVE-2014-9874",
"CVE-2014-9883",
"CVE-2015-8939",
"CVE-2015-8943",
"CVE-2016-8415",
"CVE-2016-8473",
"CVE-2016-8474",
"CVE-2017-0437",
"CVE-2017-0438",
"CVE-2017-0439",
"CVE-2017-0441",
"CVE-2017-0442",
"CVE-2017-0443",
"CVE-2017-0444",
"CVE-2017-0535",
"CVE-2017-0648",
"CVE-2017-0651",
"CVE-2017-0744",
"CVE-2017-8234",
"CVE-2017-8268"]

def most_common(lst):
    return max(set(lst), key=lst.count)

def quicksort(t):
	if t == []: return []
	else:
		pivot = t[0]
		t1 = []
		t2 = []
		for x in t[1:]:
			if x<pivot:
				t1.append(x)
			else:
				t2.append(x)
	return quicksort(t1)+[pivot]+quicksort(t2)

def commit_subj_short(string):
	remove_list = ['[media] ','UPSTREAM: ','BACKPORT: ']
	for i in remove_list:
		string = string.replace(i,"")
	return string # Don't cut it anymore

def get_kernel_rev(target):
	v1 = ["8974","8226","8960","exynos","8x60","klte","google_msm","8930","hammerhead","mako","gts2"]
	v3 = ["8996","8937","8953"]
	if any(x in target for x in v3): return 3.18
	elif any(x in target for x in v1): return 3.04
	else: return 3.10

def curlRepo(cve_id):
	curl = 'ssh -p 29418 h2o64@review.lineageos.org "gerrit query --current-patch-set (status:merged ' + cve_id + ') OR (status:open ' + cve_id + ')" | egrep "project:|number:|subject:|ref:"'
	return os.popen(curl).readlines()

def gerrit_ssh(cve_name):
	# Add manual exception (Gerrit isn't perfect)
	if cve_name == "CVE-2014-4323": return (cve_name,"Validate input arguments from user space",3.04)
	elif cve_name == "CVE-2016-8412": return (cve_name,"Adding mutex for actuator power down operations",3.10)
	tmp = curlRepo(cve_name)
	if tmp == [] : return (cve_name, "PYTHON-CVE : Commit not found")
	# Filter data
	proper_list = []
	ver_list = []
	for i in tmp:
		if "project" in i: ver_list.append(get_kernel_rev(i))
		if "subject" in i: proper_list.append(i.replace("  subject: ", "").replace("\n", ""))
	if len(tmp) == 2 : return (cve_name,commit_subj_short(tmp[1].replace("  subject: ", "").replace("\n", "")),get_kernel_rev(tmp[0]))
	new_list = []
	for j in proper_list: new_list.append(commit_subj_short(j))
	return (cve_name,most_common(list(set(new_list))),min(ver_list))

def makeCommitList(data,mod):
	commit_list = []
	n = len(data)
	i = 0
	buf = []
	# Error check
	if n%mod != 0:
		print "Error in data lenght"
		sanitizer(data,mod)
		return
	while i != n:
		if i%mod == 0:
			commit_list.append(tuple(buf))
			buf = []
		buf.append(data[i][:-1])
		i += 1
	return commit_list[1:]+[tuple(buf)]

def bestCommit(sorted_list,kernel):
	# Remove all commits from wrong linux version
	for i in sorted_list:
		if i[0] > kernel: sorted_list.remove(i)
	# Take the one with right chipset (if exists)
	chip = sys.argv[2][-7:] # MSM Only
	for j in sorted_list:
		if chip in j[1]: return j
	# Get most common subject
	target_subj = most_common([k[3] for k in sorted_list])
	# Take it from most recent linux version
	for l in reversed(sorted_list):
		if l[3] == target_subj: return l

def get_cherry(cve_id,mass):
	kernel = get_kernel_rev(sys.argv[2])
	# Get data
	data = curlRepo(cve_id)
	# Make a commit struct
	commits_list = makeCommitList(data,5)
	if commits_list == [()]: return "Commit not found in Gerrit database"
	# Remove unwanted strings
	for k in range(len(commits_list)):
		project = commits_list[k][0].replace("  project: ", "")
		number = commits_list[k][1].replace("  number: ", "")
		subject = commits_list[k][2].replace("  subject: ", "")
		patchset = commits_list[k][3].replace("    number: ", "")
		ref = commits_list[k][4].replace("    ref: ", "")
		commits_list[k] = (get_kernel_rev(project),project,number,commit_subj_short(subject),patchset,ref)
	sorted_list = quicksort(commits_list)
	best = bestCommit(sorted_list,kernel)
	if best[0] > kernel: return "No patch for this linux revision"
	if any(x in best[3] for x in blacklist):
		if mass : return ()
		else: return "Blacklisted commit"
	if mass: return best
	else: return "git fetch ssh://h2o64@review.lineageos.org:29418/" + best[1] + " " + best[5] + " && git cherry-pick FETCH_HEAD # " + best[3]

def all_cve(filename):
	tmp = open(filename, "r")
	cves = tmp.readlines()
	print 'CVE_DB = ['
	for i in cves:
		target = i[:-1]
		if target not in CVE_EXTRA_KNOWN:
			string = str(gerrit_ssh(i[:-1]))
			print string + ','
	print "]"

def is_Extra(cve_num):
	for i in CVE_DB_EXTRA:
		if cve_num == i[0]: return True
	return False

def check_for_cve(folder, suggestions, mass):
	log = list(set(os.popen('git --git-dir ' + folder + '/.git log --no-merges --since="2012-01-00" --pretty=oneline').readlines()))
	patched = []
	kernel_rev = get_kernel_rev(folder)
	mass_buf = [[],[]]
	garlic = ("yu" in folder) and ("msm8937" in folder)
	cygn_8916 = (("cyanogen" in folder) or ("qcom" in folder)) and ("msm8916" in folder)
	for commit in log:
		for cve in CVE_DB + CVE_DB_EXTRA:
			if cve[1] != "PYTHON-CVE : Commit not found" and kernel_rev >= cve[2] and cve[1] in commit[41:]:
				if not mass: print cve[0] + " patched"
				patched.append(cve[0])
	if garlic:
		for cve in GARLIC_EXCEPTION:
			print cve + " doesn't apply"
			patched.append(cve)
	if cygn_8916:
		for cve in cve_blacklist:
			print cve + " patched"
			patched.append(cve)
	for cve in CVE_DB + CVE_DB_EXTRA:
		tmp = ''
		if cve[0] not in patched and not any(x in cve[1] for x in blacklist):
			if cve[1] == "PYTHON-CVE : Commit not found" and not is_Extra(cve[0]) and not mass: print cve[0] + " commit not found"
			elif cve[1] != "PYTHON-CVE : Commit not found" and kernel_rev >= cve[2]:
				if suggestions: print get_cherry(cve[0], False) + ' # ' + cve[0]
				elif mass:
					data = get_cherry(cve[0], True)
					if data != ():
						mass_buf[0].append((data[1],data[2]))
						mass_buf[1].append((data[3],data[4],cve[0]))
				else: print cve[0] + " unpatched"
	if mass:
		for repo in list(set(mass_buf[0])):
			print "git fetch https://github.com/LineageOS/" + repo[0] + " " + repo[1]
		for commit in mass_buf[1]:
			print "git cherry-pick " + commit[1] + " # " + commit[0] + " | " + commit[2]

if __name__ == '__main__':
		if sys.argv[1] == "db" : all_cve(sys.argv[2])
		elif sys.argv[1] == "check" : check_for_cve(sys.argv[2], False, False)
		elif sys.argv[1] == "sug" : check_for_cve(sys.argv[2], True, False)
		elif sys.argv[1] == "sug-big" : check_for_cve(sys.argv[2], False, True)
		else: print "Error wrong arguments"

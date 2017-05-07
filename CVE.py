import os
import copy
import sys
from CVE_DB import *

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

def gerrit_ssh(cve_name):
	# Add manual exception (Gerrit isn't perfect)
	if cve_name == "CVE-2014-4323": return (cve_name,"msm: mdp: Validate input arguments from user space")
	elif cve_name == "CVE-2016-8412": return (cve_name,"msm: sensor: Adding mutex for actuator power down operations")
	tmp = os.popen('ssh -p 29418 h2o64@review.lineageos.org "gerrit query  (status:merged ' + cve_name + ') OR (status:open ' + cve_name + ')" | grep "subject: "').readlines()
	if tmp == [] : return (cve_name, "PYTHON-CVE : Commit not found") 
	# Filter data
	cursor = 0
	proper_list = []
	for i in tmp: proper_list.append(i.replace("  subject: ", "").replace("\n", ""))
	if len(tmp) == 1 : return (cve_name,tmp[0].replace("  subject: ", "").replace("\n", ""))
	for j in proper_list:
		j.replace("BACKPORT","")
		j.replace("UPSTREAM","")
	sorted_list = quicksort(proper_list) # Helps for duplicates
	return (cve_name,most_common(sorted_list))

def get_kernel_rev(target):
	v1 = ["8974","8226","8960","exynos","8x60","klte","google_msm"]
	v3 = ["8996","8937","8953"]
	if any(x in target for x in v3): return 3.18
	elif any(x in target for x in v1): return 3.04
	else: return 3.10

def get_cherry(cve_id):
	tmp = 'ssh -p 29418 h2o64@review.lineageos.org "gerrit query --current-patch-set (status:merged ' + cve_id + ') OR (status:open ' + cve_id + ')" | egrep "project:|number:|subject:|ref:"'
	data = os.popen(tmp).readlines()
	# Make a commit struct
	commits_list = []
	j = 0
	while j < len(data):
		# Project
		# Number
		# Subject
		# patchset (not used)
		# ref
		commits_list.append((data[j],data[j+1],data[j+2],data[j+3],data[j+4]))
		j += 5
	# Remove unwanted strings
	for k in range(len(commits_list)):
		project = (commits_list[k][0].replace("  project: ", "")).replace("\n","")
		number = (commits_list[k][1].replace("  number: ", "")).replace("\n","")
		subject = (commits_list[k][2].replace("  subject: ", "")).replace("\n","")
		patchset = (commits_list[k][3].replace("    number: ", "")).replace("\n","")
		ref = (commits_list[k][4].replace("    ref: ", "")).replace("\n","")
		commits_list[k] = (get_kernel_rev(project),project,number,subject,patchset,ref)
	sorted_list = quicksort(commits_list)
	# Get best commit for each linux rev
	best_sub = []
	old_rev = sorted_list[0][0]
	buf = []
	for commit in sorted_list:
		if commit == sorted_list[-1] and old_rev == commit[0]:
			buf.append(commit[3])
			best_sub.append((old_rev,most_common(buf)))
		elif commit[0] != old_rev :
			buf.append(commit[3])
			best_sub.append((old_rev,most_common(buf)))
			buf = []
		else: buf.append(commit[3])
		old_rev = commit[0]
	# Convert back into larger data struct
	target_picks = []
	for goal in best_sub: # TODO: To optimize
		for commit in sorted_list:
			if (commit[0],commit[3]) == goal:
				target_picks.append(commit)
				break
	# Select THE commit based on kernel rev
	picked = target_picks[0]
	avail_ver = [i[0] for i in target_picks]
	kernel = get_kernel_rev(sys.argv[2])
	if kernel in avail_ver: pref = kernel
	elif kernel < min(avail_ver): return "No patch for this linux revision"
	else: pref = max(avail_ver)
	for j in range(len(target_picks)):
		if target_picks[j][0] == pref: num = j
	cmd = "git fetch ssh://h2o64@review.lineageos.org:29418/" + target_picks[num][1] + " " + target_picks[num][5] + " && git cherry-pick FETCH_HEAD # " + target_picks[num][3]
	return cmd

'''
def multiprocess_cve(cve_list):
	# Make the Pool of workers
	pool = ThreadPool(8)
	results = pool.map(gerrit_ssh, cve_list)
	print results
	pool.close()
	pool.join()
'''

def all_cve(filename):
	tmp = open(filename, "r")
	cves = tmp.readlines()
	print 'CVE_DB = ['
	for i in cves:
		string = str(gerrit_ssh(i[:-1]))
		print string + ','
	print "]"

def check_for_cve(folder, suggestions):
	git_path = folder
	log = set(os.popen('git --git-dir ' + git_path + '/.git log --no-merges --since="2013-01-00" --pretty=oneline').readlines())
	patched = []
	for commit in log:
		for cve in CVE_DB:
			if cve[1] in commit[41:]:
				print cve[0] + " patched"
				patched.append(cve[0])
	for cve in CVE_DB:
		tmp = ''
		if cve[0] not in patched:
			if cve[1] == "PYTHON-CVE : Commit not found" : print cve[0] + " commit not found"
			else:
				if suggestions: print get_cherry(cve[0]) + ' # ' + cve[0]
				else: print cve[0] + " unpatched"


if __name__ == '__main__':
		if sys.argv[1] == "db" : all_cve(sys.argv[2])
		elif sys.argv[1] == "check" : check_for_cve(sys.argv[2], False)
		elif sys.argv[1] == "sug" : check_for_cve(sys.argv[2], True)
		else: print "Error wrong arguments"

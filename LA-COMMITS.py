from __future__ import division
import datetime
import os
import copy

target = ["LineageOS/android_device_cyanogen_msm8916-common",
"LineageOS/android_device_yu_tomato",
"LineageOS/android_device_yu_lettuce",
"LineageOS/android_device_yu_jalebi",
"LineageOS/android_device_xiaomi_msm8996-common",
"LineageOS/android_device_xiaomi_gemini",
"LineageOS/android_kernel_xiaomi_msm8996"]

# Blacklist
commit_blacklist = ['166134'] # 8916-common: LineageDoze
commit_blacklist += ['178189'] # gemini: NXP NFC Config
commit_blacklist += ['167062','167063','167064'] # xiaomi: sRGB
commit_blacklist += ['165010','175706'] # xiaomi : Network mode
commit_blacklist += ['181121','181132'] # xiaomi : AOSP NFC
commit_blacklist += ['177764'] # xiaomi : SVELTE
commit_blacklist += ['183033'] # xiaomi : EAP
commit_blacklist += ['172543'] # xiaomi : CGroup RT Bandwith (broken)
commit_blacklist += ['160575'] # jalebi: LCD Hooks (thermal)
commit_blacklist += ['178216'] # lettuce : CNE/DPM
commit_blacklist += ['170873','170878','170879','170880','172113','170876','170877','170874','170875','182882','182883'] # tomato : VoLTE
commit_blacklist += ['177854'] # tomato: CNE/DPM
commit_blacklist += ['180232','181606'] # xiaomi_kernel : Temporary blacklist (I fucked up)

# Gerrit extra commits
gerrit_extra = []

# Github extra commits
github_extra = []

# Sumbmit command
#sumbit_command = 'gerrit review --code-review +1'
sumbit_command = ''

# Helpers

# Taken from http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python/8778548#8778548
# and http://stackoverflow.com/questions/19068269/how-to-convert-a-string-date-into-datetime-format-in-python
def totimestamp(dt, epoch=datetime.datetime(1970,1,1)):
    td = dt - epoch
    return td.total_seconds()

def utctotimestamp(string):
	return totimestamp(datetime.datetime.strptime(string[:len(string)-4], "%Y-%m-%d %H:%M:%S"))

min_date = utctotimestamp("2017-01-25 00:00:00 UTC")

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

def curlRepo(name):
			curl = 'ssh -p 29418 h2o64@review.lineageos.org gerrit query --current-patch-set status:open ' + name + ' | egrep "project:|number:|subject:|lastUpdated:|ref:"'
			return os.popen(curl).readlines()

# Detects which commits is the bitch
def sanitizer(data,mod):
	i = 0
	while i < len(data):
		if not "project" in data[i]:
			for j in range(i-2*mod,i+2*mod):
				print str(j) + " | " + str(j%mod) + " # " + data[j][:-1]
			return
		i += 6

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

def gather():
		# Download data
		data = []
		# Download data
		for repo in target: data += curlRepo('project:' + repo)
		# Get personnal misc commits
		data += curlRepo('owner:"theh2o64@gmail.com"')
		# Download extra commits
		if gerrit_extra != []:
			for extra in gerrit_extra: data += curlRepo('change:' + extra)
		# Make a commit struct
		commits_list = makeCommitList(data,6)
		# Remove unwanted strings
		buf = []
		for k in range(len(commits_list)):
			number = commits_list[k][1].replace("  number: ", "")
			if number in commit_blacklist: continue # Apply a blacklist
			project = commits_list[k][0].replace("  project: ", "")
			updated = commits_list[k][3].replace("  lastUpdated: ", "")
			subject = commits_list[k][2].replace("  subject: ", "")
			patchset = commits_list[k][4].replace("    number: ", "")
			ref = commits_list[k][5].replace("    ref: ", "")
			buf.append((project,updated,number,subject,patchset,ref)) # Add lastUpdated in higher prio
		# Convert timestamps to real time
		time_list = []
		for m in buf:
			commit_time = utctotimestamp(m[1])
			if commit_time > min_date : time_list.append((m[0],commit_time,int(m[2]),m[3],m[4],m[5]))
		# Sort everything
		time_list = quicksort(list(set(time_list)))
		return time_list


def gather_github():
	# Struct :
	# project_name
	# remote
	# commit
	# branch
	github_list = []
	for commit in github_extra:
		remote_length = 0
		for i in range(len(commit[0])):
			suffix = commit[0][:i]
			if suffix.endswith('/') and remote_length == 0 :
				remote_length = i
			elif suffix.endswith('/'): project_name = commit[0][remote_length:i-7]
		github_list.append((project_name,'https://github.com/' + commit[0][:remote_length-1] + '/' + project_name,commit[0][-40:],commit[1]))
	return github_list

# Print 'cd' a smart way
def cd_print(cd_to_print,old_cd):
	if not old_cd == cd_to_print:
		# Print CD and checks
		if old_cd == '':	print 'if [ -d "$CURRENT_DIR/' + cd_to_print + '" ]; then\n  cd $CURRENT_DIR/' + cd_to_print
		else: print 'fi\nif [ -d "$CURRENT_DIR/' + cd_to_print + '" ]; then\n  cd $CURRENT_DIR/' + cd_to_print
		old_cd = cd_to_print
	return old_cd

# Print everything
def picks():
	gerrit_list = gather()
	if github_extra != ['']: github_list = gather_github()
	old_cd = ''
	print 'CURRENT_DIR=$1'
	if sumbit_command != '':
		for gerrit_c in gerrit_list:
			print "  ssh -p 29418 h2o64@review.lineageos.org " + sumbit_command + " " + str(gerrit_c[2]) + "," + gerrit_c[4] + ' # ' + gerrit_c[5]
	else:
		for gerrit_c in gerrit_list:
			old_cd = cd_print((gerrit_c[0].replace('LineageOS/android_','')).replace('_','/'),old_cd)
			print "  git fetch ssh://h2o64@review.lineageos.org:29418/" + gerrit_c[0] + " " + gerrit_c[5] + " && git cherry-pick FETCH_HEAD # " + gerrit_c[3]
	if github_extra != ['']:
		for github_c in github_list:
			old_cd = cd_print((github_c[0].replace('android_','').replace('proprietary_','').replace('_','/') + "\ngit fetch " + github_c[1] + ' ' + github_c[3]),old_cd)
			print '  git cherry-pick ' + github_c[2]
	print 'fi\ncd $CURRENT_DIR'

if __name__ == '__main__':
    picks()

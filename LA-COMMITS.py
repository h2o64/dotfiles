from __future__ import division
import datetime
import os
import copy

curl = 'ssh -p 29418 h2o64@review.lineageos.org gerrit query --current-patch-set status:open owner:"theh2o64@gmail.com" | egrep "project:|number:|subject:|lastUpdated:|ref:"'
target = ["LineageOS/android_device_cyanogen_msm8916-common",
"LineageOS/android_kernel_cyanogen_msm8916",
"LineageOS/android_device_yu_tomato",
"LineageOS/android_device_yu_lettuce",
"LineageOS/android_device_yu_jalebi"]
target_open = ["LineageOS/android_device_xiaomi_msm8996-common",
"LineageOS/android_device_xiaomi_gemini",
"LineageOS/android_kernel_xiaomi_msm8996"]
commit_blacklist = ['163950','163951','164088','166050','165010']
commit_blacklist += ['167063','167064','165605'] # xiaomi WIP srgb and dt2w
gerrit_extra = ['']
github_extra = [('LineageOS/android_device_yu_lettuce/commit/c226459166e9f29cb6fc953ddf3e581c74c7c590','cm-14.1')]
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

def gather():
		# Download data
		data = os.popen(curl).read()
		# Download data for status:open repos
		if target_open != []:
			for repo in target_open:
				curl_open = 'ssh -p 29418 h2o64@review.lineageos.org gerrit query --current-patch-set status:open project:' + repo + ' | egrep "project:|number:|subject:|lastUpdated:|ref:"'
				data += os.popen(curl_open).read()
		if gerrit_extra != ['']:
			for extra in gerrit_extra:
				curl_extra = 'ssh -p 29418 h2o64@review.lineageos.org gerrit query --current-patch-set status:open change:' + extra + ' | egrep "project:|number:|subject:|lastUpdated:|ref:"'
				data += os.popen(curl_extra).read()
		# Filter data
		cursor = 0
		new_data = []
		for i in range(len(data)):
			if data[cursor:i].endswith('\n'):
				new_data.append(data[cursor:i-1])
				cursor = i
			if i == len(data) - 1: new_data.append(data[cursor:i])
		# Make a commit struct
		commits_list = []
		j = 0
		while j < len(new_data):
			# Project
			# Number
			# Subject
			# lastUpdated
			# patchset (not used)
			# ref
			commits_list.append((new_data[j],new_data[j+1],new_data[j+2],new_data[j+3],new_data[j+4],new_data[j+5]))
			j += 6
		# Remove unwanted strings
		for k in range(len(commits_list)):
			project = commits_list[k][0].replace("  project: ", "")
			updated = commits_list[k][3].replace("  lastUpdated: ", "")
			number = commits_list[k][1].replace("  number: ", "")
			subject = commits_list[k][2].replace("  subject: ", "")
			patchset = commits_list[k][4].replace("    number: ", "")
			ref = commits_list[k][5].replace("    ref: ", "")
			commits_list[k] = (project,updated,number,subject,patchset,ref) # Add lastUpdated in higher prio
		# Only take authorized repos
		commits_edited = []
		for l in commits_list:
			if ((l[0] in target+target_open) and (l[2] not in commit_blacklist)) or l[2] in gerrit_extra: commits_edited.append(l)
		# Convert timestamps to real time
		time_list = []
		for m in commits_edited:
			commit_time = utctotimestamp(m[1])
			if commit_time > min_date : time_list.append((m[0],commit_time,int(m[2]),m[3],m[4],m[5]))
		# Sort everything
		time_list = quicksort(time_list)
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
		old_cd = cd_to_print
		print 'cd $CURRENT_DIR/' + cd_to_print
	return old_cd

# LA-Only ?
def isLA_ONLY(project_name,old_p,old_b):
	la_bool = True
	for allowed in target:
		if project_name in allowed: la_bool = False
	if project_name in "LineageOS/android_bionic": la_bool = False
	if 'android_device_yu_' in project_name: la_bool = False
	if la_bool and project_name != old_p and not old_b: print 'if [ $CURRENT_DIR_NAME == "LA" ]; then'
	if not la_bool and project_name != old_p and old_b: print 'fi'
	old_p = project_name
	old_b = la_bool
	return (old_p,old_b)

def picks():
	gerrit_list = gather()
	github_list = gather_github()
	old_cd = ''
	old_project = ''
	old_bool = False
	print 'CURRENT_DIR=$1'
	print 'CURRENT_DIR_NAME=$(basename $CURRENT_DIR)'
	if sumbit_command != '':
		for gerrit_c in gerrit_list:
			print "ssh -p 29418 h2o64@review.lineageos.org " + sumbit_command + " " + str(gerrit_c[2]) + "," + gerrit_c[4] + ' # ' + gerrit_c[5]
	else:
		for gerrit_c in gerrit_list:
			old_project,old_bool = isLA_ONLY(gerrit_c[0],old_project,old_bool)
			old_cd = cd_print((gerrit_c[0].replace('LineageOS/android_','')).replace('_','/'),old_cd)
			print "git fetch ssh://h2o64@review.lineageos.org:29418/" + gerrit_c[0] + " " + gerrit_c[5] + " && git cherry-pick FETCH_HEAD # " + gerrit_c[3]
			if gerrit_c == gerrit_list[-1] and old_bool:
				print 'fi'
				old_bool = False
	for github_c in github_list:
		old_project,old_bool = isLA_ONLY(github_c[0].replace('/',''),old_project,old_bool)
		old_cd = cd_print((github_c[0].replace('android_','').replace('proprietary_','').replace('_','/') + "\ngit fetch " + github_c[1] + ' ' + github_c[3]),old_cd)
		print 'git cherry-pick ' + github_c[2]
		if github_c == github_list[-1] and old_bool :
			print 'fi'
			old_bool = False
	print 'cd $CURRENT_DIR'

if __name__ == '__main__':
    picks()

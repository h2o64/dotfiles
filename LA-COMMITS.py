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
"LineageOS/android_device_xiaomi_gemini"]
commit_blacklist = ['163950','163951','164088','165234','166050','163241','162818','168685']
gerrit_extra = ['169017'] # dmalloc

github_extra = [
('h2o64/proprietary_vendor_yu/commit/07fc4e31b395da7b276f09a02daffb051d361876','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/0dff53419ac9dd114f5e028c720d5ea931febd81','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/3b4fb2d2cf8b661a95b02244f33b27f4c2302601','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/d7e497f4f00c96b5d77acc496a023f05c6d4e71c','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/a5366698a7904bdb4a2781140d2ab5dd09bc8c70','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/b2d1cecffe81b88160f265bba1ebfaf8df26ff1e','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/75556a5c330d44da133fd95a21ebc26f7118b884','cm-14.1'),
('h2o64/proprietary_vendor_yu/commit/5bc5de2bb5f074d6f62c77fa8dccb492759a4943','cm-14.1-data'),
('h2o64/proprietary_vendor_yu/commit/00280883fdbe86494df5a49cc11c570a58c761db','cm-14.1-data')]

# Helpers

# Taken from http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python/8778548#8778548
# and http://stackoverflow.com/questions/19068269/how-to-convert-a-string-date-into-datetime-format-in-python
def totimestamp(dt, epoch=datetime.datetime(1970,1,1)):
    td = dt - epoch
    return td.total_seconds()

def utctotimestamp(string):
	return totimestamp(datetime.datetime.strptime(string[:len(string)-4], "%Y-%m-%d %H:%M:%S"))

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
		if gerrit_extra != []:
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
			time_list.append((m[0],utctotimestamp(m[1]),int(m[2]),m[3],m[4],m[5]))
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
	if la_bool == True and project_name != old_p and old_b == False: print 'if [ $CURRENT_DIR_NAME == "LA" ]; then'
	if la_bool == False and project_name != old_p and old_b == True: print 'fi'
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
	for gerrit_c in gerrit_list:
		old_project,old_bool = isLA_ONLY(gerrit_c[0],old_project,old_bool)
		old_cd = cd_print((gerrit_c[0].replace('LineageOS/android_','')).replace('_','/'),old_cd)
		print "git fetch ssh://h2o64@review.lineageos.org:29418/" + gerrit_c[0] + " " + gerrit_c[5] + " && git cherry-pick FETCH_HEAD # " + gerrit_c[3]
	for github_c in github_list:
		# old_project,old_bool = isLA_ONLY(github_c[0].replace('/',''),old_project,old_bool)
		old_cd = cd_print((github_c[0].replace('android_','').replace('proprietary_','').replace('_','/') + "\ngit fetch " + github_c[1] + ' ' + github_c[3]),old_cd)
		print 'git cherry-pick ' + github_c[2]
		if github_c == github_list[-1] and old_bool : print 'fi'
	print 'cd $CURRENT_DIR'

if __name__ == '__main__':
    picks()

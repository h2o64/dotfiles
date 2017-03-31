from __future__ import division
import datetime
import os
import copy

curl = 'ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query --current-patch-set status:open | egrep "project:|number:|subject:|lastUpdated:|ref:"'
commit_blacklist = ['163950','163951','164088','165234','166050']
github_extra = []

# Helpers

# Taken from http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python/8778548#8778548
# and http://stackoverflow.com/questions/19068269/how-to-convert-a-string-date-into-datetime-format-in-python
def totimestamp(dt, epoch=datetime.datetime(1970,1,1)):
    td = dt - epoch
    return td.total_seconds()

def utctotimestamp(string):
	return totimestamp(datetime.datetime.strptime(string[:len(string)-5], "%Y-%m-%d %H:%M:%S"))

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
			if l[2] not in commit_blacklist: commits_edited.append(l)
		# Convert timestamps to real time
		time_list = []
		for m in commits_edited:
			time_list.append((m[0],utctotimestamp(m[1]),m[2],m[3],m[4],m[5]))
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

def picks():
	gerrit_list = gather()
	github_list = gather_github()
	old_cd = ''
	old_project = ''
	old_bool = False
	print 'CURRENT_DIR=$1'
	print 'CURRENT_DIR_NAME=$(basename $CURRENT_DIR)'
	for gerrit_c in gerrit_list:
		if gerrit_c[0] == 'yu-community-os/android_external_fsck_msdos':
			old_cd = cd_print(('external/fsck_msdos'),old_cd)
		elif gerrit_c[0] == 'yu-community-os/android_external_wpa_supplicant_8':
			old_cd = cd_print(('external/wpa_supplicant_8'),old_cd)
		else:
			old_cd = cd_print((gerrit_c[0].replace('yu-community-os/android_','').replace('yu-community-os/proprietary_','')).replace('_','/'),old_cd)
		print "git fetch ssh://h2o64@gerrit.aosparadox.org:29418/" + gerrit_c[0] + " " + gerrit_c[5] + " && git cherry-pick FETCH_HEAD # " + gerrit_c[3]
	for github_c in github_list:
		old_cd = cd_print((github_c[0].replace('android_','').replace('proprietary_','').replace('_','/') + "\ngit fetch " + github_c[1] + ' ' + github_c[3]),old_cd)
		print 'git cherry-pick ' + github_c[2]
	print 'cd $CURRENT_DIR'

if __name__ == '__main__':
    picks()

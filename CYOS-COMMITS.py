from __future__ import division
import datetime
import os
import copy

curl = 'curl -s --request GET http://gerrit.aosparadox.org/changes/?q=status:open+project:yu-community-os/'
target = ["android",
"android_art",
"android_bionic",
"android_build",
"android_build_kati",
"android_device_cyanogen_msm8916-common",
"android_device_qcom_common",
"android_device_qcom_sepolicy",
"android_device_yu_jalebi",
"android_device_yu_lettuce",
"android_device_yu_tomato",
"android_external_e2fsprogs",
"android_external_f2fs-tools",
"android_external_fsck_msdos",
"android_external_jemalloc",
"android_external_libjpeg-turbo",
"android_external_libnfc-nci",
"android_external_libpng",
"android_external_skia",
"android_external_sqlite",
"android_external_tinyalsa",
"android_external_tinycompress",
"android_external_wpa_supplicant_8",
"android_external_zlib",
"android_frameworks_av",
"android_frameworks_base",
"android_frameworks_native",
"android_frameworks_opt_net_wifi",
"android_frameworks_opt_telephony",
"android_frameworks_rs",
"android_gcc_linux-x86_aarch64_aarch64-linux-android-4.9",
"android_gcc_linux-x86_arm-linux-android-4.9",
"android_hardware_libhardware",
"android_hardware_qcom_bt",
"android_hardware_qcom_wlan",
"android_hardware_ril",
"android_kernel_yu_msm8916",
"android_packages_apps_Dialer",
"android_packages_apps_FMRadio",
"android_packages_apps_PackageInstaller",
"android_packages_apps_PhoneCommon",
"android_packages_apps_Settings",
"android_packages_apps_SnapdragonCamera",
"android_packages_apps_SnapdragonGallery",
"android_packages_inputmethods_LatinIME",
"android_packages_providers_MediaProvider",
"android_packages_services_Telecomm",
"android_packages_services_Telephony",
"android_system_bt",
"android_system_core",
"android_system_extras",
"android_system_media",
"android_system_sepolicy",
"android_system_vold",
"android_vendor_qcom_opensource_bluetooth"
"android_vendor_qcom_opensource_fm",
"android_vendor_volte",
"proprietary_vendor_yu"]
la_only_target = []

# Blacklisting
commit_blacklist = [[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]
word_blacklist = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
id_black_per_rom = ['']
rom_black_per_rom = ['']

# Extra commits
github_extra = ['']
github_extra_branch = ['']
gerrit_extra = ['']

# Global variables
repos_count = len(target)
commits_count = [0]*repos_count
gerritReset = False

# Taken from http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python/8778548#8778548
# and http://stackoverflow.com/questions/19068269/how-to-convert-a-string-date-into-datetime-format-in-python
def totimestamp(dt, epoch=datetime.datetime(1970,1,1)):
    td = dt - epoch
    return td.total_seconds()

def utctotimestamp(string):
	return totimestamp(datetime.datetime.strptime(string[:len(string)-4], "%Y-%m-%d %H:%M:%S.%f"))

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

def get_patchset(commit_id):
	tmp = os.popen('ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query change:' + commit_id + ' --current-patch-set | grep "number: " | grep -v "' + commit_id + '"').read()
	return ((tmp.replace('number: ', '')).replace('\n','')).replace(' ','')

def filter(liste):
	# Filter data
	tmp_liste = []
	cursor = 0
	for k in range(len(liste)):
		# print 'k = ' + str(k) + ' cursor = ' + str(cursor) + ' liste[cursor:k] = ' + liste[cursor:k]
		if liste[cursor:k].endswith('\n'):
			tmp_liste.append(liste[cursor:k-1])
			cursor = k
		if k == len(liste) - 1: tmp_liste.append(liste[cursor:k])
	return tmp_liste

def gather(remotes):
	project_out = []
	numbers_out = []
	subject_out = []
	topic_out = []
	updated_out = []
	count = 0
	new_curl = ''
	remo = ''
	# Gather raw data
	for i in remotes:
		if i.startswith('open'):
			remo = i[4:]
			new_curl = 'curl -s --request GET http://gerrit.aosparadox.org/changes/?q=status:open+project:yu-community-os/'
		else:
			remo = i
			new_curl = curl
		project_out.append('yu-community-os/' + remo)
		numbers_out.append(os.popen(new_curl + remo + '| sed 1d | jq --raw-output ".[] | ._number"').read())
		topic_out.append(os.popen(new_curl + remo + '| sed 1d | jq --raw-output ".[] | .topic"').read())
		subject_out.append(os.popen(new_curl + remo + '| sed 1d | jq --raw-output ".[] | .subject"').read())
		updated_out.append(os.popen(new_curl + remo + '| sed 1d | jq --raw-output ".[] | .updated"').read())
		count += 1
	return (project_out,topic_out,numbers_out,subject_out,updated_out)

# Filter and un-split
def split(project_global, topic_global, numbers_global, subject_global,updated_global):
	project_local = [0]*repos_count
	topic_local = [0]*repos_count
	numbers_local = [0]*repos_count
	subject_local = [0]*repos_count
	updated_local = [0]*repos_count
	for k in range(repos_count):
		project_local[k] = project_global[k]
		topic_local[k] = filter(topic_global[k])
		numbers_local[k] = filter(numbers_global[k])
		subject_local[k] = filter(subject_global[k])
		updated_local[k] = filter(updated_global[k])
		# print 'k = ' + str(k) + ' | numbers_local[k] = ' + str(numbers_local[k])
	return (project_local,topic_local,numbers_local,subject_local,updated_local)

# Print data
def results():
	project_global,topic_global,numbers_global,subject_global,updated_global = gather(target)
	project,topic,numbers,subject,updated = split(project_global, topic_global, numbers_global, subject_global,updated_global)
	for k in range(repos_count):
		for j in range(commits_count[k]):
			print('#####################')
			print('Project : ' + project[k])
			print('Change number : ' + numbers[k][j])
			print('Subject : ' + subject[k][j])
			print('Last updated : ' + updated[k][j])
			print('Timestamp : ' + str(utctotimestamp(updated[k][j])))
			if not topic[k][j] == 'null': print('Topic : ' + topic[k][j])
	for l in range(repos_count):
		print 'Number of commits for ' + project[l] + ' = ' + str(len(numbers[l]))

# Filtering to show last updated last
def order(topic_fil,numbers_fil,subject_fil,updated_fil):
	new_time = copy.deepcopy(updated_fil)
	dummy_copy = copy.deepcopy(updated_fil)
	new_time_sorted = copy.deepcopy(updated_fil)
	# Keep UTC alphabetic time sorted
	for k in range(repos_count): new_time_sorted[k] = quicksort(updated_fil[k])
	# Convert the timestamp UTC to numerical
	for k in range(repos_count):
		for j in range(commits_count[k]):
			new_time[k][j] = (utctotimestamp(dummy_copy[k][j]),k,j)
	# Sort numerical timestamp
	for k in range(repos_count): new_time[k] = copy.deepcopy(quicksort(new_time[k]))
	# print str(new_time)
	topic_new = copy.deepcopy(topic_fil)
	numbers_new = copy.deepcopy(numbers_fil)
	subject_new = copy.deepcopy(subject_fil)
	time_swap(topic_fil, topic_new, new_time, new_time_sorted, dummy_copy)
	time_swap(numbers_fil, numbers_new, new_time, new_time_sorted, dummy_copy)
	time_swap(subject_fil, subject_new, new_time, new_time_sorted, dummy_copy)
	return topic_new,numbers_new,subject_new,new_time_sorted

def time_swap(old, new, time_ref, new_time_bis, old_time):
	for k in range(repos_count):
		for j in range(commits_count[k]):
			# print 'old time = ' + str(old_time[k][j]) + ' | new time = ' + str(new_time_bis[k][j])
			new = old[time_ref[k][j][1]][time_ref[k][j][2]]

# Print 'cd' a smart way
def cd_print(cd_to_print,old):
	if not old == cd_to_print:
		old = cd_to_print
		print 'cd $CURRENT_DIR' + cd_to_print
	return old

# LA-Only ?
def isLA_ONLY(project_name):
	count = 0
	# print '# LA CHECK #'
	# print 'project_name = ' + project_name
	for i in la_only_target:
		# print 'target = ' + target[i]
		if target[i].startswith('open') and (target[i][4:] in project_name): return True
		elif target[i] in project_name: return True
	tmp = project_name.replace('yu-community-os/','')
	# print "Second method"
	# print "tmp = " + tmp
	for j in target:
		# print "j = " + j
		if tmp in j: return False
	return True

# Cherry picks
def picks():
	project_global,topic_global,numbers_global,subject_global,updated_global = gather(target)
	project,topic,numbers,subject,updated = split(project_global, topic_global, numbers_global, subject_global,updated_global)
	for k in range(repos_count): commits_count[k] = len(numbers[k])
	topic,numbers,subject,updated = order(topic,numbers,subject,updated)
	ret_topic = [0]*repos_count
	ret_numbers = [0]*repos_count
	ret_subject = [0]*repos_count
	git_fetch = 'git fetch ssh://h2o64@gerrit.aosparadox.org:29418/'
	banned_rom_ind = []
	tmp = 'if '
	blacklist_word_count = [0]*repos_count
	word_blacklist_bool = True
	old_cd = ''
	print 'CURRENT_DIR=$1'
	print 'CURRENT_DIR_NAME=$(basename $CURRENT_DIR)'
	for k in range(repos_count):
		# Reverse everything to show min first
		# TODO: Fix this in quicksort
		ret_topic[k] = copy.deepcopy(topic[k][::-1])
		ret_numbers[k] = copy.deepcopy(numbers[k][::-1])
		ret_subject[k] = copy.deepcopy(subject[k][::-1])
		if isLA_ONLY(project[k]): print 'if [ $CURRENT_DIR_NAME == "LA" ]; then'
		old_cd = cd_print(project[k].replace('yu-community-os/android', '').replace('_','/'),old_cd)
		if gerritReset:
			print 'git remote remove gerrit'
			print 'git remote add gerrit ssh://h2o64@gerrit.aosparadox.org:29418/' + project[k]
			print 'git fetch gerrit cyos-7.1\ngit reset --hard gerrit/cyos-7.1'
		for j in range(commits_count[k]):
			if word_blacklist[k] not in ret_subject[k][j]:
				blacklist_word_count[k] += - 1
				word_blacklist_bool = False
			if ret_numbers[k][j] not in commit_blacklist[k]: # or word_blacklist_bool:
				for i in range(len(id_black_per_rom)):
					if ret_numbers[k][j] == id_black_per_rom[i]: banned_rom_ind.append(i)
				for m in banned_rom_ind:
					tmp += '[ ! $CURRENT_DIR_NAME == "' + rom_black_per_rom[m] + '" ]'
					if not m == banned_rom_ind[len(banned_rom_ind)-1]: tmp += ' || '
				if ret_numbers[k][j] in id_black_per_rom: print tmp + '; then'
				tmp = 'if '
				print git_fetch + project[k] + ' refs/changes/' + ret_numbers[k][j][-2] + ret_numbers[k][j][-1] + '/' + ret_numbers[k][j] + '/' + get_patchset(ret_numbers[k][j]) +' && git cherry-pick FETCH_HEAD # ' + ret_subject[k][j] # + ' - ' + updated[k][j]
				if ret_numbers[k][j] in id_black_per_rom: print 'fi'
			# Reset
			word_blacklist_bool = True
			banned_rom_ind = []
		if gerritReset: print 'git push gerrit HEAD:refs/for/cyos-7.1' # cyos-7.1 hardcoded because idc
		if isLA_ONLY(project[k]): print 'fi'
	cherry = ''
	suffix = ''
	is_proprietary = False
	first_LA = 1
	if not '' in github_extra:
		for ind in range(len(github_extra)):
			commit = github_extra[ind]
			for i in range(len(commit)):
				suffix = copy.deepcopy(commit[i:])
				if suffix.startswith('proprietary_vendor_'): is_proprietary = True
				if suffix.startswith('android_') or is_proprietary:
					suffix = copy.deepcopy(suffix[:len(suffix)-8-40])
					# print "# INFO #"
					# print "isLA_ONLY(suffix) = " + str(isLA_ONLY(suffix))
					# print "first_LA = " + str(first_LA)
					# print "ind = " + str(ind)
					# print "len(github_extra) = " + str(len(github_extra))
					if isLA_ONLY(suffix) and first_LA == 1:
						print 'if [ $CURRENT_DIR_NAME == "LA" ]; then'
						first_LA = 2
					elif not isLA_ONLY(suffix) and first_LA == 2:
						print 'fi'
						first_LA = 1
					if is_proprietary:
						cd = ('/' + suffix.replace('proprietary_','')).replace('_','/')
					else:
						cd = ('/' + suffix.replace('android_','')).replace('_','/')
					cd =  cd + '\n' + 'git fetch http://github.com/' + commit[:-40-8] +  ' ' + github_extra_branch[ind]
					old_cd = cd_print(cd,old_cd)
					print 'git cherry-pick ' + commit[-40:]
					if isLA_ONLY(suffix) and ind == len(github_extra)-1: print 'fi'
					# Reset
					cherry = ''
					suffix = ''
					break
			is_proprietary = False
	commit_details = []
	first_LA = 1
	if not '' in gerrit_extra:
		for m in gerrit_extra:
			tmp = os.popen('ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query change:' + m + ' | grep "project: "').read() # Project
			commit_details.append(((tmp.replace('project: ', '')).replace('\n','')).replace(' ',''))
			tmp = os.popen('ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query change:' + m + ' --current-patch-set | grep "number: " | grep -v "' + m + '"').read() # Patchset
			commit_details.append(((tmp.replace('number: ', '')).replace('\n','')).replace(' ',''))
			tmp = os.popen('ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query change:' + m + ' | grep "commitMessage: "').read() # Subject
			commit_details.append((tmp.replace('commitMessage: ', '')).replace('\n',''))
			tmp = os.popen('ssh -p 29418 h2o64@gerrit.aosparadox.org gerrit query change:' + m + ' | grep "lastUpdated: "').read() # Updated
			commit_details.append((tmp.replace('lastUpdated: ', '')).replace('\n',''))
			# print "# INFO #"
			# print "isLA_ONLY(commit_details[0]) = " + str(isLA_ONLY(commit_details[0]))
			# print "first_LA = " + str(first_LA)
			# print "m = " + m
			# print "gerrit_extra[-1] = " + gerrit_extra[-1]
			if isLA_ONLY(commit_details[0]) and first_LA == 1:
				print 'if [ $CURRENT_DIR_NAME == "LA" ]; then'
				first_LA = 2
			elif not isLA_ONLY(commit_details[0]) and first_LA == 2:
				print "Enter second condition"
				print 'fi'
				first_LA = 1
			old_cd = cd_print(commit_details[0].replace('yu-community-os/android', '').replace('_','/'),old_cd)
			print git_fetch + commit_details[0] + ' refs/changes/' + m[-2] + m[-1] + '/' + m + '/' + commit_details[1] +' && git cherry-pick FETCH_HEAD #' + commit_details[2] # + ' - ' + commit_details[3]
			if isLA_ONLY(commit_details[0]) and m == gerrit_extra[-1]: print 'fi'
			commit_details = [] # Reset
	for l in range(repos_count):
		print '# Number of commits for ' + project[l] + ' = ' + str(len(ret_numbers[l]) - len(commit_blacklist[l]) + blacklist_word_count[l])
	print '# Number of extra commits  = ' + str(len(github_extra) + len(gerrit_extra))
	print 'cd $CURRENT_DIR'

if __name__ == '__main__':
    picks()

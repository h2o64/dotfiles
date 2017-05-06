# -*- coding: utf-8 -*-

import os
import copy
import sys
from CVE_DB import *

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
	tmp = os.popen('ssh -p 29418 h2o64@review.lineageos.org gerrit query ' + cve_name + ' | grep "subject: "').read()
	if tmp == '' : return
	# Filter data
	cursor = 0
	proper_list = []
	for i in range(len(tmp)):
		if tmp[cursor:i].endswith('\n'):
			proper_list.append((tmp[cursor:i-1]).replace("  subject: ", ""))
			cursor = i
		if i == len(tmp) - 1: proper_list.append(tmp[cursor:i])
	sorted_list = quicksort(proper_list) # Helps for duplicates
	# Get most occured string
	max_length = 0
	length = 0
	old_item = proper_list[0]
	best = ''
	for item in proper_list:
		if item == old_item: length += 1
		else:
					if max_length <= length:
						max_length = length
						best = old_item
						length = 0
		old_item = item
	if best != '' : return (cve_name,best)

'''
def multiprocess_cve(cve_list):
	# Make the Pool of workers
	pool = ThreadPool(8)
	results = pool.map(gerrit_ssh, cve_list)
	print results
	pool.close()
	pool.join()
'''

def all_cve(argv):
	filename = sys.argv[1]
	tmp = open(filename, "r")
	cves = tmp.readlines()
	print 'CVE_DB = ['
	for i in cves:
		string = str(gerrit_ssh(i[:-1]))
		if string != 'None' : print str(gerrit_ssh(i[:-1])) + ','
	print "]"

def check_for_cve(argv):
	git_path = sys.argv[1]
	log = os.popen('git --git-dir ' + git_path + '/.git log --since="2013-01-00"--pretty=oneline').readlines()
	patched = []
	#print log
	for commit in log:
		for cve in CVE_DB:
			if cve[1] in commit:
				print cve[0] + " patched"
				patched.append(cve[0])
	for cve in CVE_DB:
		if cve[0] not in patched: print cve[0] + " unpatched"

if __name__ == '__main__':
    check_for_cve(sys.argv)


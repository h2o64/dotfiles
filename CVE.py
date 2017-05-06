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
	tmp = os.popen('ssh -p 29418 h2o64@review.lineageos.org gerrit query ' + cve_name + ' | grep "subject: "').readlines()
	if tmp == [] : return (cve_name, "PYTHON-CVE : Commit not found") 
	# Filter data
	cursor = 0
	proper_list = []
	for i in tmp: proper_list.append(i.replace("  subject: ", "").replace("\n", ""))
	if len(tmp) == 1 : return (cve_name,tmp[0].replace("  subject: ", "").replace("\n", ""))
	sorted_list = quicksort(proper_list) # Helps for duplicates
	# Get most occured string
	max_length = 0
	length = 0
	old_item = proper_list[0]
	best = proper_list[0]
	for item in proper_list:
		if item == old_item:
			length += 1
			if max_length <= length:
				max_length = length
				best = item
		else:
			length = 0
		if item == proper_list[-1] and max_length <= length :	
			best = item
		old_item = item
	return (cve_name,best)

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
	filename = sys.argv[2]
	tmp = open(filename, "r")
	cves = tmp.readlines()
	print 'CVE_DB = ['
	for i in cves:
		string = str(gerrit_ssh(i[:-1]))
		print string + ','
	print "]"

def check_for_cve(argv):
	git_path = sys.argv[2]
	log = os.popen('git --git-dir ' + git_path + '/.git log --since="2013-01-00"--pretty=oneline').readlines()
	patched = []
	#print log
	for commit in log:
		for cve in CVE_DB:
			if cve[1] == "PYTHON-CVE : Commit not found" : print cve[0] + " commit not found"
			elif cve[1] in commit:
				print cve[0] + " patched"
				patched.append(cve[0])
	for cve in CVE_DB:
		if cve[0] not in patched: print cve[0] + " unpatched"

if __name__ == '__main__':
		if sys.argv[1] == "db" : all_cve(sys.argv)
		elif sys.argv[1] == "check" : check_for_cve(sys.argv)
		else: print "Error wrong arguments"


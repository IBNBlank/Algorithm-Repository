# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 20:03:04

################
##### good #####
################

import time

def dup2(A):
	"""Assuming A is a sorted list.
		Return true if A has duplicated"""
	for i in range(len(A)-1):
		if A[i] == A[i+1]:
			return True
	return False

if __name__ == '__main__':
	start = time.time()

	N = 100000
	A = list(range(N))
	print(dup2(A))

	print(time.time() - start)
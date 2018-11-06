# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 20:03:12

####################
##### pythonic #####
####################

import time

def dup3(A):
	"""Assuming A is a sorted list.
		Return true if A has duplicated"""
	return True if len(A) == len(set(A)) else False

if __name__ == '__main__':
	start = time.time()

	N = 100000
	A = list(range(N))
	print(dup3(A))

	print(time.time() - start)
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-26 20:29:33

###############
##### bad #####
###############

import time

def dup1(A):
	for i in range(len(A)-1):
		for j in range(i+1, len(A)):
			if A[i] == A[j]:
				return True
	return False


if __name__ == '__main__':
	start = time.time()

	N = 100000
	A = list(range(N))
	print(dup1(A))

	print(time.time() - start)
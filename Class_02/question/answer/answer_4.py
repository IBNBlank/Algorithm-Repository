# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:34:35

combination = []

def permutation(arr, index, count):
	global combination
	if count == 1:
		for i in range(index+1, 0, -1):
			combination.append(i)
			print(combination)
			combination.pop()
	elif index>0:
		combination.append(arr[index])
		permutation(arr, index - 1, count- 1)
		combination.pop()
		permutation(arr, index - 1, count)

n = int(input())
m = int(input())
permutation([i for i in range(1, n+1)], n-1, m)
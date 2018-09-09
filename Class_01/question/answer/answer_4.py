# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-15 12:08:50
def sub_sum(arr, index, target):
	if target == 0:
		return True
	elif index == 0:
		return arr[0] == target
	elif arr[index] > target:
		return sub_sum(arr, index - 1, target)
	else:
		return sub_sum(arr, index - 1, target - arr[index]) or sub_sum(arr, index - 1, target)


s = input().split(' ')
target = int(input())
array = [int(i) for i in s]
index = len(array) - 1
print(sub_sum(array, index, target))
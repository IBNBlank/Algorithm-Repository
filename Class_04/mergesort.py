# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-02 20:40:39

import time

def mergesort(nums):
	if len(nums) <= 1:
		return nums
	mid = int(len(nums)/2)
	left = mergesort(nums[:mid])
	right = mergesort(nums[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

if __name__ == '__main__':
	N = int(input())
	nums = list(range(N, 0, -1))

	start = time.time()

	print(mergesort(nums))

	print(time.time() - start)
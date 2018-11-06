# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 19:37:33

###################
##### 排序算法 #####
###################

##### 选择排序 #####
# 最佳时间复杂度: Θ(N^2)
# 最坏时间复杂度: Θ(N^2)
# 空间复杂度: Θ(1)
def selection_sort(seq):
	if len(seq) <= 1:
		return seq
	for i in range(len(seq)-1):
		min_index = i
		for j in range(i+1, len(seq)):
			if seq[min_index] > seq[j]:
				min_index = j
		if min_index != i:
			seq[min_index], seq[i] = seq[i], seq[min_index]
	return seq

##### 冒泡排序 #####
# 最佳时间复杂度: Θ(N^2)
# 最坏时间复杂度: Θ(N^2)
# 空间复杂度: Θ(1)
def bubble_sort(seq):
	if len(seq) <= 1:
		return seq
	for i in range(len(seq)-1):
		for j in range(i+1, len(seq)):
			if seq[i] > seq[j]:
				seq[i], seq[j] = seq[j], seq[i]
	return seq

##### 就地堆排序 #####
# 最佳时间复杂度: Θ(N)*
# 最坏时间复杂度: Θ(NlogN)
# 空间复杂度: Θ(1)



##### 归并排序 #####
# 最佳时间复杂度: Θ(NlogN)
# 最坏时间复杂度: Θ(NlogN)
# 空间复杂度: Θ(N)

def merge_sort(seq):
	if len(seq) <= 1:
		return seq
	mid = int(len(seq)/2)
	left = merge_sort(seq[:mid])
	right = merge_sort(seq[mid:])
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

##### 就地插入排序 #####
# 最佳时间复杂度: Θ(N)
# 最坏时间复杂度: Θ(N^2)
# 空间复杂度: Θ(1)



##### 快速排序 #####
# 最佳时间复杂度: Θ(NlogN)
# 最坏时间复杂度: Θ(N^2)
# 空间复杂度: Θ(logN)

def quick_sort_1(start_index, end_index):
	if start_index >= end_index:
		return
	global a
	store_index = start_index + 1
	for i in range(start_index+1, end_index):
		if a[i] < a[start_index]:
			a[i], a[store_index] = a[store_index], a[i]
			store_index += 1
	a[start_index], a[store_index-1] = a[store_index-1], a[start_index]

	qsort_1(start_index, store_index-1)
	qsort_1(store_index, end_index)

def quick_sort_2(seq):
	if len(seq) <= 1:
		return seq

	store_index = 1
	for i in range(1, len(seq)):
		if seq[i] < seq[0]:
			seq[i], seq[store_index] = seq[store_index], seq[i]
			store_index += 1
	seq[0], seq[store_index-1] = seq[store_index-1], seq[0]

	left = qsort_2(seq[0:store_index-1])
	right = qsort_2(seq[store_index:len(seq)])

	return left + [seq[store_index-1]] + right
	return left + right

def quick_sort_mid_p(seq):
	if len(seq) <= 1:
		return seq

	mid_index = len(seq) // 2
	seq[0], seq[mid_index] = seq[mid_index], seq[0]

	store_index = 1
	for i in range(1, len(seq)):
		if seq[i] < seq[0]:
			seq[i], seq[store_index] = seq[store_index], seq[i]
			store_index += 1
	seq[0], seq[store_index-1] = seq[store_index-1], seq[0]

	left = qsort_mid_p(seq[0:store_index-1])
	right = qsort_mid_p(seq[store_index:len(seq)])

	return left + [seq[store_index-1]] + right

if __name__ == '__main__':
	a = [5, 9, 8, 7, 6, 10, 4, 3, 2, 1]
	print(qsort_2(a))
	print(qsort_mid_p(a))
	qsort_1(0, len(a))
	print(a)
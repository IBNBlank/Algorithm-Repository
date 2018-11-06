# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-25 14:22:44
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:50:08

def merge_sort(seq):
	if len(seq) == 1:
		return seq, 0

	mid_index = len(seq) // 2
	left_seq = seq[0:mid_index]
	right_seq = seq[mid_index:]

	left_seq, left_count = merge_sort(left_seq)
	right_seq, right_count = merge_sort(right_seq)

	merge_count = 0
	merge_seq = []

	while left_seq and right_seq:
		if left_seq[0] <= right_seq[0]:
			merge_seq.append(left_seq.pop(0))
		else:
			merge_seq.append(right_seq.pop(0))
			merge_count += len(left_seq)

	merge_seq += left_seq + right_seq

	final_count = left_count + right_count + merge_count
	return merge_seq, final_count


s = input()
# s = '4 3 2 1'
s_list = s.split(' ')
nums = [int(i) for i in s_list]
sort_nums, count = merge_sort(nums)
print(count)
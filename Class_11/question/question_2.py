# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:46:54

# 描述
# 给定一些区间，将其中重合的部分合并起来。
# 比如[1,3], [2,4], [3,6], [8,9]，可以合并为[1,6], [8,9]两个区间。
# 不可以用系统自带的sort()方法。

# 输入
# 一行数据，包含多个区间，区间之间用空格隔开，区间的开始和结束数字用:隔开，比如：
# 1:3 2:4 3:6 8:9

# 输出
# 多行数据，每一行表示一个合并后的区间，区间的开始和结束用:隔开。
# 注意区间要按照从小到大的顺序输出。

# 输入样例 1：
# 1:3 2:4 3:6 8:9

# 输出样例 1：
# 1:6
# 8:9

class MathSet(object):
	def __init__(self, string):
		self.min, self.max = string.split(":")
		self.min = int(self.min)
		self.max = int(self.max)

	def __lt__(self, mathset):
		return self.min < mathset.min

	def __eq__(self, mathset):
		return (self.min == mathset.min) and (self.max == mathset.max)

	def __str__(self):
		return "{}:{}".format(self.min, self.max)

def merge_mathset(mathset_1, mathset_2):
	if mathset_2.min >= mathset_1.min:
		if mathset_2.min <= mathset_1.max:
			mathset_2.min = mathset_1.min
			mathset_2.max = max(mathset_1.max, mathset_2.max)
			return True
	elif mathset_2.max >= mathset_1.min:
		mathset_2.max = max(mathset_1.max, mathset_2.max)
		return True
	else:
		return False

def qsort_mid_p(seq):
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
	set_list = []
	origin_sets = input().split(' ')

	for origin_set in origin_sets:
		new = MathSet(origin_set)
		remove_list = []
		for mathset in set_list:
			if merge_mathset(mathset, new):
				remove_list.append(mathset)
		for mathset in remove_list:
			set_list.remove(mathset)
		set_list.append(new)

	set_list = qsort_mid_p(set_list)

	for final_set in set_list:
		print(final_set)
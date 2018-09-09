# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-14 11:49:42
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-20 12:26:05

##### 求子列表 #####
def subset(lists):
	length = len(lists)
	count = 2 ** length
	temp = []
	subsets = []
	for i in range(count):
		temp = []
		for j in range(length):
			if i & (1<<j):
				temp.append(lists[j])
		subsets.append(temp)
	return subsets

if __name__ == '__main__':
	s = input()
	lists = s.split(' ')

	print(subset(lists))
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 01:07:39

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

class SeedFilling(object):
	def __init__(self, num, img):
		self.__img = img
		self.__num = num
		self.__label_num = 0
		self.__pass()

	def __pass(self):
		for y in range(self.__num):
			for x in range(self.__num):
				if self.__img[y][x] == 1:
					self.__label_num += 1
					self.__mark(x, y)

	def __mark(self, x, y):
		self.__img[y][x] = 2
		if y != 0:
			if self.__img[y-1][x] == 1:
				self.__mark(x, y-1)

		if y != self.__num-1:
			if self.__img[y+1][x] == 1:
				self.__mark(x, y+1)

		if x != 0:
			if self.__img[y][x-1] == 1:
				self.__mark(x-1, y)

		if x != self.__num-1:
			if self.__img[y][x+1] == 1:
				self.__mark(x+1, y)

	def get_label(self):
		return self.__label_num

if __name__ == '__main__':
	img = []
	num = int(input())
	for _ in range(num):
		cache = input()
		img_row = [int(item) for item in cache]
		img.append(img_row)

	sf = SeedFilling(num, img)
	print(sf.get_label())
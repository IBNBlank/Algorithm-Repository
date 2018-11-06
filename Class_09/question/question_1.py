# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-29 21:14:36

# 描述
# 给定一组数字An和一个数m，要求用课上所学完成一个最小堆结构来储存该数组。
# 然后执行m次删除最小数操作，最后输出最小数。

# 输入
# 第一行为一组数字，每个数字之间用空格隔开，最多有100000个数字。
# 第二行为一个数字，表示m。

# 输出
# 执行m次删除最小数操作后堆中最小数

# 输入样例：
# 3 1 2 5 3 2 4
# 3

# 输出样例：
# 3

class PriorityQueue(object):
	def __init__(self):
		self.__queue = [None]
		self.__size = 0

	def get_smallest(self):
		return self.__queue[1]

	def get_size(self):
		return self.__size

	def add(self, i):
		self.__size += 1
		self.__queue.append(i)
		self.__swim(self.__size)

	def remove_smallest(self):
		if self.__size > 1:
			self.__size -= 1
			data = self.__queue.pop()
			self.__queue[1] = data
			self.__sink(1)
		elif self.__size == 1:
			self.__size -= 1
			self.__queue.pop()

	def __swim(self, index):
		if index > 1:
			parent_index = self.__parent(index)
			if self.__queue[parent_index] > self.__queue[index]:
				self.__swap(index, parent_index)
				self.__swim(parent_index)

	def __sink(self, index):
		child = self.__left_child(index)
		if child > self.__size:
			return
		elif child == self.__size:
			if self.__queue[index] > self.__queue[child]:
				self.__swap(index, child)
		else:
			if self.__queue[child] > self.__queue[child+1]:
				child += 1
			if self.__queue[index] > self.__queue[child]:
				self.__swap(index, child)
				self.__sink(child)

	def __swap(self, index_1, index_2):
		self.__queue[index_1], self.__queue[index_2] = self.__queue[index_2], self.__queue[index_1]

	def __left_child(self, index):
		return index * 2

	def __right_child(self, index):
		return index * 2 + 1

	def __parent(self, index):
		return index // 2

if __name__ == '__main__':
	num_list = input().split(' ')
	times = int(input())

	pq = PriorityQueue()
	for i in num_list:
		pq.add(int(i))

	for _ in range(times):
		pq.remove_smallest()

	print(pq.get_smallest())
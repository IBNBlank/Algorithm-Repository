# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-05 01:44:18
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-21 23:35:28
class MaxHeap(object):
	"""docstring for Heap"""
	def __init__(self):
		self.__keys = [None]
		self.__size = 0

	def add(self, x):
		self.__keys.append(x)
		self.__size += 1
		self.__swim_up(self.__size)

	def get_biggest(self):
		if self.__size > 0:
			return self.__keys[1]
		else:
			return None

	def remove_biggest(self):
		if self.__size > 1:
			self.__keys[1] = self.__keys.pop()
			self.__size -= 1
			self.__swim_down(1)
		elif self.__size > 0:
			self.__keys.pop()
			self.__size -= 1

	def size(self):
		return self.__size

	def __swim_up(self, index):
		if index == 1:
			return

		parent_index = index // 2
		if self.__keys[parent_index] < self.__keys[index]:
			self.__swap(index, parent_index)
			self.__swim_up(parent_index)

	def __swim_down(self, index):
		left_child_index = index * 2
		right_child_index = index * 2 + 1
		swim_down_index = index

		# 判断有没有左子节点
		if left_child_index <= self.__size:
			if self.__keys[index] < self.__keys[left_child_index]:
				swim_down_index = left_child_index

		# 判断有没有右子节点
		if right_child_index <= self.__size:
			if self.__keys[index] < self.__keys[right_child_index]:

				# 判断右节点的数据是不是更小，始终往更小的那个子节点游过去
				if self.__keys[left_child_index] < self.__keys[right_child_index]:
					swim_down_index = right_child_index

		# 如果swim_down_index还是index没有变
		# 说明要么没有子节点，要么子节点都更大
		# 那么当前节点不用再往下游了，否则继续
		if swim_down_index != index:
			self.__swap(index, swim_down_index)
			self.__swim_down(swim_down_index)

	def __swap(self, a, b):
		self.__keys[a], self.__keys[b] = self.__keys[b], self.__keys[a]

	def print(self):
		print(self.__keys[1:])


s = input()
m = int(input())
# s = '3 1 2 4 6 2 3 4 2 7 8 10 4'
# m = 5
heap = MaxHeap()
items = s.split(' ')
for item in items:
	if heap.size() < m:
		heap.add(int(item))
	elif int(item) < heap.get_biggest():
		heap.remove_biggest()
		heap.add(int(item))

s = ''
while heap.get_biggest() is not None:
	s += str(heap.get_biggest()) + ' '
	heap.remove_biggest()
print(s)
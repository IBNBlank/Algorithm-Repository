# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-29 21:15:08

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
	pq = PriorityQueue()

	for i in range(10):
		pq.add(10-i)
		print(10-i)

	print("")
	print("===test===")
	print("==t1==")

	print(pq.get_size())
	print(pq.get_smallest())

	print("==t2==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t3==")

	pq.add(100)
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t4==")

	pq.add(0)
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t5==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t6==")

	pq.add(0)
	pq.add(0)
	pq.add(0)
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t7==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t8==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t9==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t10==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t11==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())

	print("==t12==")

	pq.remove_smallest()
	print(pq.get_size())
	print(pq.get_smallest())
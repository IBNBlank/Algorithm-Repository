# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-05 01:44:18
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 16:11:23

class IntNode(object):
	"""docstring for IntNode"""
	def __init__(self, i, h, n, p):
		self.item = i
		self.hash_code = h
		self.next = n
		self.prev = p

class DLList(object):
	"""docstring for SLList"""
	def __init__(self, x=None):
		self.__sentinel = IntNode(49, 0, None, None)
		self.__sentinel.next = self.__sentinel
		self.__sentinel.prev = self.__sentinel
		self.__last = self.__sentinel.prev
		if x is None:
			self.__size = 0
		else:
			self.__sentinel.next = IntNode(x, self.__sentinel, self.__sentinel)
			self.__sentinel.prev = self.__sentinel.next
			self.__size = 1

	def get_first(self):
		return self.__sentinel.next.item

	def get_items(self):
		p = self.__sentinel
		while p.next is not self.__sentinel:
			p = p.next
			yield (p.item, p.hash_code)

	def contains(self, x):
		p = self.__sentinel
		while p.next is not self.__sentinel:
			p = p.next
			if p.item == x:
				return True
		return False

	def add_last(self, x, h):
		self.__size += 1
		self.__sentinel.prev = IntNode(x, h, self.__sentinel, self.__sentinel.prev)
		self.__sentinel.prev.prev.next = self.__sentinel.prev

	def size(self):
		return self.__size

class DataIndexedStringSet(object):
	"""docstring for DataIndexedStringSet"""
	def __init__(self):
		# 用 [DLList()] * 4 是有问题的，思考一下为什么
		self.__present = [DLList() for _ in range(4)]
		self.__m = 4
		self.__size = 0

	def add(self, x):
		hash_code = hash(x)
		index = hash_code % self.__m
		self.__present[index].add_last(x, hash_code)
		self.__size += 1
		if self.__size / self.__m > 1.5:
			self.__resize()

	def contains(self, x):
		hash_code = hash(x)
		index = hash_code % self.__m
		return self.__present[index].contains(x)

	def __resize(self):
		self.__m *= 2
		new_map = [DLList() for _ in range(self.__m)]
		for l in self.__present:
			for item, hash_code in l.get_items():
				index = hash_code % self.__m
				new_map[index].add_last(item, hash_code)

		self.__present = new_map

diss = DataIndexedStringSet()
add_n = int(input())
for _ in range(add_n):
	item = input()
	diss.add(item)
check_n = int(input())
for _ in range(check_n):
	item = input()
	print(diss.contains(item))
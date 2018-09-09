# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:30:23
class IntNode(object):
	"""docstring for IntNode"""
	def __init__(self, i, n, p):
		self.item = i
		self.next = n
		self.prev = p

class DLList(object):
	"""docstring for SLList"""
	def __init__(self, x=None):
		self.__sentinel = IntNode(49, None, None)
		self.__sentinel.next = self.__sentinel
		self.__sentinel.prev = self.__sentinel
		self.__last = self.__sentinel.prev
		if x is None:
			self.__size = 0
		else:
			self.__sentinel.next = IntNode(x, self.__sentinel, self.__sentinel)
			self.__sentinel.prev = self.__sentinel.next
			self.__size = 1

	def add_first(self, x):
		self.__sentinel.next = IntNode(x, self.__sentinel.next, self.__sentinel)
		self.__sentinel.next.next.prev = self.__sentinel.next
		self.__size += 1

	def get_first(self):
		return self.__sentinel.next.item

	def add_last(self, x):
		self.__size += 1
		self.__sentinel.prev = IntNode(x, self.__sentinel, self.__sentinel.prev)
		self.__sentinel.prev.prev.next = self.__sentinel.prev

	def insert(self, num, x):
		self.__size += 1
		p = self.__sentinel.next
		count = 0
		while count < num:
			p = p.next
			count += 1

		new_node = IntNode(x, p.next, p)
		p.next.prev = new_node
		p.next = new_node

	def size(self):
		return self.__size

	def output(self):
		s = ''
		p = self.__sentinel.next
		count = 0
		while count < self.__size - 1:
			s += p.item + '->'
			p = p.next
			count += 1
		s += p.item
		print(s)

s1 = input()
s2 = input()

s_list = s1.split(' ')
l = DLList()
for item in s_list:
	l.add_last(item)

s2 = s2.split(' ')
num = int(s2[0])
item = s2[1]

l.insert(num, item)
l.output()
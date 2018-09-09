# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 20:07:11
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-20 15:40:56

class IntNode(object):
	def __init__(self, i, n, p):
		self.item = i
		self.next = n
		self.prev = p

class DLList(object):
	def __init__(self):
		self.__sentinel = IntNode(None, None, None)
		self.__sentinel.next = self.__sentinel
		self.__sentinel.prev = self.__sentinel
		self.__size = 0

	##### 开头结尾 #####
	def add_first(self, x=None):
		self.__sentinel.next = IntNode(x, self.__sentinel.next, self.__sentinel)
		self.__sentinel.next.next.prev = self.__sentinel.next
		self.__size += 1

	def add_last(self, x=None):
		self.__sentinel.prev = IntNode(x, self.__sentinel, self.__sentinel.prev)
		self.__sentinel.prev.prev.next = self.__sentinel.prev
		self.__size += 1

	def remove_first(self):
		self.__sentinel.next = self.__sentinel.next.next
		self.__sentinel.next.prev = self.__sentinel
		self.__size -= 1

	def remove_last(self):
		self.__sentinel.prev = self.__sentinel.prev.prev
		self.__sentinel.prev.next = self.__sentinel
		self.__size -= 1

	##### 整体属性 #####
	def get_size(self):
		return self.__size

	def get_all(self):
		datas = []
		p = self.__sentinel
		while p.next is not self.__sentinel:
			p = p.next
			datas.append(p.item)
		return datas

	def get_all_reverse(self):
		datas = []
		p = self.__sentinel
		while p.prev is not self.__sentinel:
			p = p.prev
			datas.append(p.item)
		return datas

	##### 特定对象 #####
	def __pointer_forward(self, num):
		p = self.__sentinel.next
		for i in range(num):
			p = p.next
		return p

	def __pointer_backward(self, num):
		p = self.__sentinel
		for x in range(self.__size-num):
			p = p.prev
		return p

	def __insert_forward(self, num, value):
		p = self.__pointer_forward(num)
		p.prev.next = IntNode(value, p, p.prev)
		p.prev = p.prev.next
		self.__size += 1

	def __insert_backward(self, num, value):
		p = self.__pointer_backward(num)
		p.prev.next = IntNode(value, p, p.prev)
		p.prev = p.prev.next
		self.__size += 1

	def __remove_forward(self, num):
		p = self.__pointer_forward(num)
		p.prev.next = p.next
		p.next.prev = p.prev
		self.__size -= 1

	def __remove_backward(self, num):
		p = self.__pointer_backward(num)
		p.prev.next = p.next
		p.next.prev = p.prev
		self.__size -= 1

	def __get_forward(self, num):
		p = self.__pointer_forward(num)
		return p.item

	def __get_backward(self, num):
		p = self.__pointer_backward(num)
		return p.item

	def __set_forward(self, num, value):
		p = self.__pointer_forward(num)
		p.item = value

	def __set_backward(self, num, value):
		p = self.__pointer_backward(num)
		p.item = value

	def insert_chosen(self, num=0, value=None):
		if num > self.__size or num < 0:
			print("GET_ERROR")
			return 0
		elif num < self.__size/2:
			self.__insert_forward(num, value)
		else:
			self.__insert_backward(num, value)

	def remove_chosen(self, num=0):
		if num >= self.__size or num < 0:
			print("GET_ERROR")
			return 0
		elif num < self.__size/2:
			self.__remove_forward(num)
		else:
			self.__remove_backward(num)

	def get_chosen(self, num=0):
		if num >= self.__size or num < 0:
			print("GET_ERROR")
			return 0
		elif num < self.__size/2:
			return self.__get_forward(num)
		else:
			return self.__get_backward(num)

	def set_chosen(self, num=0, value=None):
		if num >= self.__size or num < 0:
			print("GET_ERROR")
			return 0
		elif num < self.__size/2:
			return self.__set_forward(num, value)
		else:
			return self.__set_backward(num, value)

if __name__ == '__main__':
	l = DLList()
	nums = int(input())

	for num in range(nums):
		l.add_last(num)

	print("SIZE:{}".format(l.get_size()))

	print(l.get_all())
	print(l.get_all_reverse())

	print(l.get_chosen(1))
	print(l.get_chosen(nums-2))

	l.set_chosen(1, 666)
	l.set_chosen(nums-2, 666)

	print(l.get_all())

	l.insert_chosen(nums-1, 777)
	l.insert_chosen(1, 777)

	print(l.get_all())

	print("SIZE:{}".format(l.get_size()))

	l.remove_chosen(l.get_size()-2)
	l.remove_chosen(1)

	print(l.get_all())

	print("SIZE:{}".format(l.get_size()))
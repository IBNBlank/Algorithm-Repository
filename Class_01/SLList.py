# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-15 12:55:06
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-20 13:06:54

class IntNode(object):
	def __init__(self, i, n):
		self.item = i
		self.next = n

class SLList(object):
	def __init__(self):
		self.__sentinel = IntNode(None, None)
		self.__last = self.__sentinel
		self.__size = 0

	def add(self, x=None):
		self.__sentinel.next = IntNode(x, self.__sentinel.next)
		if self.__last is self.__sentinel:
			self.__last = self.__sentinel.next
		self.__size += 1

	def add_last(self, x=None):
		temp = self.__last
		self.__last = IntNode(x, None)
		temp.next = self.__last
		self.__size += 1

	### 缓存 ###
	def get_size(self):
		return self.__size

	### 非递归 ###
	# def get_size(self):
	# 	total_size = 0
	# 	p = self.__sentinel
	# 	while p.next is not None:
	# 		total_size += 1
	# 		p = p.next
	# 	return total_size

	### 递归 ###
	# def __get_size(self, p):
	# 	if p is None:
	# 		return 0
	# 	else:
	# 		return 1 + self.__get_size(p.next)

	# def get_size(self):
	# 	return self.__get_size(self.__sentinel.next)

	def get_all(self):
		datas = []
		p = self.__sentinel
		while p.next is not None:
			p = p.next
			datas.append(p.item)
		return datas

	def get_chosen(self, num=0):
		if num < self.__size:
			p = self.__sentinel.next
			for i in range(num):
				p = p.next
			return p.item
		else:
			print("GET_ERROR")
			return 0

	def set_chosen(self, num=0, value=0):
		if num < self.__size:
			p = self.__sentinel.next
			for i in range(num):
				p = p.next
			p.item = value
		else:
			print("GET_ERROR")

if __name__ == '__main__':
	l = SLList()
	nums = int(input())

	l.add_last(666)

	for num in range(nums):
		l.add(num)

	print("SIZE:{}".format(l.get_size()))

	print(l.get_all())
	print(l.get_chosen(nums-1))

	l.set_chosen(nums-1, nums)

	l.add_last(666)

	print(l.get_all())
	print(l.get_chosen(nums-1))
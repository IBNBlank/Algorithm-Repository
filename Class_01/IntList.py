# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 20:01:19
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-13 22:19:05

##### 链表 #####
class IntList(object):
	def __init__(self, f, r):
		self.first = f
		self.rest = r

	### 查询大小 ###
	## 递归 ##
	def iterate_size(self):
		if self.rest is None:
			return 1
		else:
			return 1 + self.rest.iterate_size()
	## 非递归 ##
	def size(self):
		p = self
		total_size = 1
		while p.rest is not None:
			p = p.rest
			total_size += 1
		return total_size

	### 查询元素 ###
	## 递归 ##
	def iterate_get(self, i=0):
		if i == 0:
			return self.first
		else:
			return self.rest.iterate_get(i-1)
	## 非递归 ##
	def get(self, i=0):
		p = self
		for x in range(i):
			p = p.self
		return p.first


if __name__ == '__main__':
	l = IntList(5, None)
	l = IntList(10, l)
	l = IntList(15, l)

	print(l.get(0))
	print(l.iterate_get(0))
	print(l.size())
	print(l.iterate_size())
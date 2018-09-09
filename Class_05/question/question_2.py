# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 14:20:07

class WeightedQuickUnionDS(object):
	def __init__(self, N):
		self.__root_id = list(range(N))
		self.__weight = [1]*N

	def is_connected(self, p, q):
		return self.__root(p) == self.__root(q)

	def connect(self, p, q):
		root_p = self.__root(p)
		root_q = self.__root(q)

		if self.__weight[root_p] < self.__weight[root_q]:
			self.__root_id[root_p] = root_q
			self.__weight[root_q] += self.__weight[root_p]
		else:
			self.__root_id[root_q] = root_p
			self.__weight[root_p] += self.__weight[root_q]

	def __root(self, p):
		while self.__root_id[p] != p:
			p = self.__root_id[p]
		return p

N = int(input())
ds = WeightedQuickUnionDS(N)
n = int(input())
for _ in range(n):
	s = input()
	a, b = s.split(' ')
	a = int(a)
	b = int(b)
	ds.connect(a, b)
m = int(input())
for _ in range(m):
	s = input()
	a, b = s.split(' ')
	a = int(a)
	b = int(b)
	print(ds.is_connected(a, b))
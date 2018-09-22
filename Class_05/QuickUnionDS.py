# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 19:25:55
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 19:28:06

class QuickUnionDS(object):
	def __init__(self, N):
		self.__root_id = list(range(N))

	def is_connected(self, p, q):
		return self.__root(p) == self.__root(q)

	def connect(self, p, q):
		self.__root_id[self.__root(p)] = self.__root(q)

	def __root(self, p):
		while self.__root_id[p] != p:
			p = self.__root_id[p]
		return p

if __name__ == '__main__':
	N = 10
	ds = QuickUnionDS(N)

	for i in range(N-1):
		ds.connect(i, i+1)

	for i in range(N-1):
		print(ds.is_connected(i, i+1))
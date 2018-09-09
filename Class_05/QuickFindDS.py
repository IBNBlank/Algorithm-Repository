# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 12:15:40

class QuickFindDS(object):
	def __init__(self, N):
		self.__id = list(range(0, N))

	def is_connected(self, p, q):
		return self.__id[p] == self.__id[q]

	def connect(self, p, q):
		pid = self.__id[p]
		qid = self.__id[q]
		self.__id = [qid if x == pid else x for x in self.__id]

N = int(input())
ds = QuickUnionDS(N)
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
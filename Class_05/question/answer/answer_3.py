# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:13:52
class WQUPCDS(object):
	def __init__(self, N):
		self.__id = list(range(0, N))
		self.__size = [1 for _ in range(N)]

	def __get_root(self, p):
		pid = self.__id[p]
		while pid != self.__id[pid]:
			pid = self.__id[pid]

		return pid

	def is_connected(self, p, q):
		p_root = self.__get_root(p)
		pid = p
		while pid != self.__id[pid]:
			parent = self.__id[pid]
			self.__id[pid] = p_root
			pid = parent

		q_root = self.__get_root(q)
		qid = q
		while qid!= self.__id[qid]:
			parent = self.__id[qid]
			self.__id[qid] = q_root
			qid = parent

		return pid == qid

	def connect(self, p, q):
		p_root = self.__get_root(p)
		q_root = self.__get_root(q)

		if self.__size[p_root] > self.__size[q_root]:
			self.__id[q_root] = self.__id[p_root]
			self.__size[p_root] += self.__size[q_root]
		else:
			self.__id[p_root] = self.__id[q_root]
			self.__size[q_root] += self.__size[p_root]

N = int(input())
ds = WQUPCDS(N)
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
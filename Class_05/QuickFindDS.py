# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 19:26:24

class QuickFindDS(object):
	def __init__(self, N):
		self.__id = list(range(0, N))

	def is_connected(self, p, q):
		return self.__id[p] == self.__id[q]

	def connect(self, p, q):
		pid = self.__id[p]
		qid = self.__id[q]
		self.__id = [qid if x == pid else x for x in self.__id]

if __name__ == '__main__':
	N = 10
	ds = QuickFindDS(N)

	for i in range(N-1):
		ds.connect(i, i+1)

	for i in range(N-1):
		print(ds.is_connected(i, i+1))
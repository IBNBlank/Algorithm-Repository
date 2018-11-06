# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 19:15:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 20:27:53

class WQUPCDS(object):
	def __init__(self, N):
		self.__root_id = list(range(N))
		self.__weight = [1] * N

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
		change_list = []
		last_weight = 0
		temp_weight = 0
		while self.__root_id[p] != p:
			change_list.append(p)
			temp_weight = last_weight
			last_weight = self.__weight[p]
			self.__weight[p] -= temp_weight
			p = self.__root_id[p]
		for item in change_list:
			self.__root_id[item] = p
		return p

if __name__ == '__main__':
	N = 10
	ds = WQUPCDS(N)

	for i in range(N-1):
		ds.connect(i, i+1)

	for i in range(N-1):
		print(ds.is_connected(i, i+1))
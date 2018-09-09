# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 17:16:42

class WQUPCDS(object):
	def __init__(self, N):
		self.__root_id = list(range(N))
		self.__weight = [1]*N

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
		while self.__root_id[p] != p:
			change_list.append(p)
			p = self.__root_id[p]
		for item in change_list:
			self.__root_id[item] = p
		return p

	def show_roots(self):
		num = 0
		for i in range(N):
			if self.__root_id[i] == i:
				num += 1
		print(num)

if __name__ == '__main__':
	N = int(input())
	ds = WQUPCDS(N)
	n = int(input())
	for _ in range(n):
		s = input()
		a, b = s.split(' ')
		a = int(a)
		b = int(b)
		ds.connect(a, b)
	ds.show_roots()
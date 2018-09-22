# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:28:28

# 描述
# 请实现一个Josh课上所介绍的WeightedQuickUnionDS，然后完成测试。

# 输入
# 第1行有一个数字，表示最大可能的数字N，N最大为50000
# 第2行有一个数字n，表示接下来有多少行数据，n最大为70000
# 第3行到第n+2行，每行有两个数字，表示连接这两个点
# 第n+3行有一个数字m，表示接下来有多少行数据，m最大为50000
# 第n+4行开始到第n+m+3行，每行有两个数字，需要输出这两个数字是否有连接

# 输出
# m行数据，用True或者False来表示输入数据中m对测试数据是否有连接

# 输入样例：
# 7
# 5
# 0 1
# 1 2
# 0 4
# 3 5
# 2 5
# 2
# 0 2
# 0 6

# 输出样例：
# True
# False

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
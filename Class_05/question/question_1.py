# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 14:07:25

# 描述：
# 输入A、B，输出A+B。

# 输入：
# 输入的第一行包括两个整数，由空格分隔，分别表示A、B。

# 输出：
# 输出一行，包括一个整数，表示A+B的值。A、B以及A+B的和均在Int范围内。

# 输入样例：
# 12 34

# 输出样例：
# 46

###################
### 没事别乱迭代 ###
###################

##### QUESTION 1 #####
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
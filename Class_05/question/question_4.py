# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:31:45

# 描述
# 作为一个数据分析师，你对你的用户中朋友圈的数量非常感兴趣。
# 现在你从后台可以看到用户数量是n，同时你可以从调查中了解到一共有m对好友关系。
# 如果两个人互相都是朋友，或者是朋友的朋友的朋友……，即直接认识或间接认识，那么认为这两个人属于一个朋友圈。
# 请问你的用户中有多少个朋友圈？

# 输入
# 第1行有一个数字n，表示用户总数量，n最大为100000。
# 第2行有一个数字m，表示接下来有多少对朋友关系，m最大为200000。
# 第3行到第m+2行，每行有两个数字，表示这两个用户认识

# 输出
# 一个数字，有多少个朋友圈

# 输入样例：
# 10
# 5
# 9 0
# 8 1
# 5 3
# 9 5
# 3 5

# 输出样例：
# 6

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
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 21:51:12

# 描述
# 有N个学生的数据，将学生数据按成绩高低排序，如果成绩相同则按姓名字符的字母序排序，
# 如果姓名的字母序也相同则按照学生的年龄排序，并输出N个学生排序后的信息。
# 不可以用系统自带的sort()方法。

# 输入
# 第一行有一个整数N（N<=8000），接下来的N行包括N个学生的数据。
# 每个学生的数据包括姓名（长度不超过10的字符串）、年龄（整形数）、成绩（小于等于100的正数）。

# 输出
# 将学生信息按成绩进行排序，成绩相同的则按姓名的字母序进行排序。
# 然后输出学生信息，按照如下格式：
# 姓名 年龄 成绩

# 输入样例 1：
# 3
# zhao 19 90
# qian 20 90
# sun 19 100

# 输出样例 1：
# qian 20 90
# zhao 19 90
# sun 19 100

class DirGraph(object):
	def __init__(self):
		self.vertices = 0
		self.root = None
		self.champion_flag = False
		self.marked = []
		self.in_adj = {}
		self.out_adj = {}

	def add_edge(self, v, w):
		if v in self.out_adj.keys():
			self.out_adj[v].append(w)
		else:
			self.out_adj.update({v:[w]})
			self.in_adj.update({v:[]})
			self.vertices += 1

		if w in self.in_adj.keys():
			self.in_adj[w].append(v)
		else:
			self.in_adj.update({w:[v]})
			self.out_adj.update({w:[]})
			self.vertices += 1

	def scan_champion(self):
		root_num = 0
		for key, value in self.in_adj.items():
			if not value:
				self.root = key
				root_num += 1
		if root_num == 1:
			self.champion_flag = True

	def dfs(self, v):
		if v in self.marked:
			return False
		elif self.out_adj[v] is None:
			return True
		else:
			self.marked.append(v)
			flag = True
			for w in self.out_adj[v]:
				flag = flag and self.dfs(w)
				self.marked.pop()
			return flag

	def is_finish(self):
		self.scan_champion()
		if self.champion_flag:
			return self.dfs(self.root)
		else:
			return False

if __name__ == '__main__':
	num = int(input())
	dg = DirGraph()
	for _ in range(num):
		win, loss = input().split(" ")
		dg.add_edge(win, loss)

	print(dg.is_finish())
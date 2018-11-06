# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 20:27:55

class NoDirGraph(object):
	def __init__(self, vertices):
		self.vertices = vertices
		self.adj = [[] for _ in range(vertices)]

	def add_edge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)

	def get_adj(self, v): # 相邻结点
		return self.adj[v]

	def get_v_nums(self):
		return self.vertices

	def get_e_nums(self):
		count = 0
		for e in self.adj:
			count += len(e)
		return nums // 2

class Paths(object):
	def __init__(self, g, s):
		self.graph = g
		self.start = s
		self.edge_to = [None for _ in range(g.get_v_nums())]
		self.marked = [False for _ in range(g.get_v_nums())]
		self.dfs(s)

	def dfs(self, v):
		self.marked[v] = True
		if self.graph.adj[v] is not None:
			for w in self.graph.adj[v]:
				if not self.marked[w]:
					self.edge_to[w] = v
					self.dfs(w)

	def has_path_to(self, v):
		return self.marked[v]

	def path_to(self, v):
		path = [v]
		v_now = v
		while self.edge_to[v_now] is not None:
			v_now = edge_to[v_now]
			path.append(v_now)
		path.reverse()
		return path

class DirGraph(object):
	def __init__(self, vertices):
		self.vertices = 1
		self.in_adj = [[] for _ in range(vertices)]
		self.out_adj = [[] for _ in range(vertices)]

	def add_edge(self, v, w):
		self.in_adj[w].append(v)
		self.out_adj[v].append(w)

	def get_adj(self, v): # 相邻结点
		return self.adj[v]

	def get_v_nums(self):
		return self.vertices

	def get_e_nums(self):
		count = 0
		for e in self.adj:
			count += len(e)
		return nums

if __name__ == '__main__':
	graph = NoDirGraph(3)
	graph = DirGraph(3)
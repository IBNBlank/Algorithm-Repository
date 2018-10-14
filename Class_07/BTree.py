# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-02 22:01:42

class Node:
	def __init__(self, data, par = None):
		print("Node __init__: " + str(data))
		self.data = list([data])
		self.parent = par
		self.child = list()

	def __str__(self):
		if self.parent:
			return str(self.parent.data) + ' : ' + str(self.data)
		return 'Root : ' + str(self.data)

	def __lt__(self, node):
		return self.data[0] < node.data[0]

	def _isLeaf(self):
		return len(self.child) == 0

	# 将新节点及其子树合并到当前节点中
	def _add(self, new_node):
		for data in new_node.data:
			if data in self.data:
				return False
		for child in new_node.child:
			child.parent = self
		self.data.extend(new_node.data)
		self.data.sort()
		self.child.extend(new_node.child)
		if len(self.child) > 1:
			self.child.sort()
		if len(self.data) > 2:
			self._split()

		return True

	# 找到正确的节点来将新节点插入到树里
	def _insert(self, new_node):
		print('Node _insert: ' + str(new_node.data) + ' into ' + str(self.data))
		# 如果该节点是叶节点，则直接将数据添加到当前节点
		if self._isLeaf():
			self._add(new_node)

		# 如果该节点不是叶节点，则找到合适的子节点继续递归搜索
		elif new_node.data[0] > self.data[-1]:
			self.child[-1]._insert(new_node)
		else:
			for i in range(0, len(self.data)):
				if new_node.data[0] < self.data[i]:
					self.child[i]._insert(new_node)
					break

	# 一个节点中已有3个元素，需要分裂节点
	# 将节点分裂为新的子树并添加到父节点中
	def _split(self):
		print("Node _split: " + str(self.data))
		left_child = Node(self.data[0], self)
		right_child = Node(self.data[2], self)
		if self.child:
			self.child[0].parent = left_child
			self.child[1].parent = left_child
			self.child[2].parent = right_child
			self.child[3].parent = right_child
			left_child.child = [self.child[0], self.child[1]]
			right_child.child = [self.child[2], self.child[3]]

		self.child = [left_child, right_child]
		self.data = [self.data[1]]

		# 现在有了新的子树，即self。
		# 需要将该节点添加到父节点中
		if self.parent:
			if self in self.parent.child:
				self.parent.child.remove(self)
			self.parent._add(self)
		else:
			left_child.parent = self
			right_child.parent = self

	# 查找一个树中的元素并返回
	# 如果未找到则返回False
	def _find(self, item):
		print("Find " + str(item))
		if item in self.data:
			return item
		elif self._isLeaf():
			return False
		elif item > self.data[-1]:
			return self.child[-1]._find(item)
		else:
			for i in range(len(self.data)):
				if item < self.data[i]:
					return self.child[i]._find(item)

	# 输出先序遍历结果
	def _preorder(self):
		print(self)
		for child in self.child:
			child._preorder()

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, item):
		if self.root is None:
			self.root = Node(item)
		else:
			self.root._insert(Node(item))
			while self.root.parent:
				self.root = self.root.parent

	def find(self, item):
		return self.root._find(item)

	def printTop2Tiers(self):
		print('----Top 2 Tiers----')
		print(str(self.root.data))
		for child in self.root.child:
			print(str(child.data), end=' ')
		print(' ')

	def preorder(self):
		print('----Preorder----')
		self.root._preorder()

tree = Tree()

lst = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]
# lst = [1,2,3,1,3,6,2]
for item in lst:
	tree.insert(item)
tree.preorder()
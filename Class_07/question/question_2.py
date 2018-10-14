# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 16:20:57

# 描述
# 给定一个数组顺序，根据该顺序生成23树，计算其中满节点（即含有两个元素的节点）的个数。

# 输入
# 一行数据，包含多个数字，数字之间用空格隔开，最多有60000个数字。

# 输出
# 一个数字，23树中满节点（即含有两个元素的节点）的个数。

# 输入样例：
# 1 4 2 5 4 3 2 2 5 2

# 输出样例：
# 1

class BST(object):
	def __init__(self, key, left=None, right=None):
		self.left = left
		self.right = right
		self.label = key

def bst_add(tree, key):
	if tree is None:
		return BST(key)
	if key < tree.label:
		tree.left = bst_add(tree.left, key)
	elif key > tree.label:
		tree.right = bst_add(tree.right, key)
	return tree

def bst_height(tree):
	if tree is None:
		return 0
	else:
		return 1 + max(bst_height(tree.left), bst_height(tree.right))

if __name__ == '__main__':
	tree = None
	nums = input().split(" ")
	for num in nums:
		tree = bst_add(tree, int(num))
	print(bst_height(tree))
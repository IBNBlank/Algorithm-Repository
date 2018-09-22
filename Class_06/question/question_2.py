# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:20:42

# 描述
# 给定一串数字，按照给定顺序建立起二叉树，求这个二叉树的高度。

# 输入
# 一行数据，一串数字，个数最多为80000。

# 输出
# 一个数字，表示二叉树的高度。

# 输入样例：
# 4 3 1 2 5 6 8 7

# 输出样例：
# 5

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
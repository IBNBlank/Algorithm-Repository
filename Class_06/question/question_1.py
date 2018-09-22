# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:19:29

# 描述
# 给定一串数字，利用二叉树的数据结构来实现一个集合。输出集合中不重复的元素个数。
# 注意不要想复杂了！这里只要求输出集合中不重复元素的个数。

# 输入
# 一行数据，包含多个数字，数字之间用空格隔开，最多有80000个数字。

# 输出
# 一个数字，集合里有多少个不重复的元素。

# 输入样例：
# 1 2 3 4 5 1 2 3

# 输出样例：
# 5

##### QUESTION 1 #####
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

def bst_size(tree):
	if tree is None:
		return 0
	else:
		return 1 + bst_size(tree.left) + bst_size(tree.right)

if __name__ == '__main__':
	tree = None
	nums = input().split(" ")
	for num in nums:
		tree = bst_add(tree, int(num))
	print(bst_size(tree))
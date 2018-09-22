# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:22:31

# 描述
# 给定一串数字，按照顺序生成二叉树，然后输出从根节点到最右边节点的路径。

# 输入
# 一行数据，一串数字，个数最多为80000。

# 输出
# 用->连接的最右路径，一行。

# 输入样例：
# 4 2 1 3 6 5 7

# 输出样例：
# 4->6->7

string = ""

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

def bst_right(tree):
	global string
	if tree is None:
		print(string[:-2])
	else:
		string += "{}->".format(tree.label)
		bst_right(tree.right)

if __name__ == '__main__':
	tree = None
	nums = input().split(" ")
	for num in nums:
		tree = bst_add(tree, int(num))
	bst_right(tree)
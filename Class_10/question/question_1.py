# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-23 22:11:54

# 描述
# 给定一组数字，按顺序添加到二叉搜索树内，然后按照指定格式要求打印树的结构。
# 重复的元素应忽略。

# 输入
# 一行数据，多个数字以空格隔开。
# 数字最多为100000个，均为整数。

# 输出
# 输出格式如下：
# · 每行有一个节点
# · 第n层节点前有n*2个空格
# · 左子树节点先输出，右子树节点后输出
# 对于一颗如下结构的树：
#     4
#    / \
#   2   5
#  / \
# 1   3
# 输出的结果应该为：
# 4
#   2
#     1
#     3
#   5

# 输入样例 1：
# 4 2 1 3 5

# 输出样例 1：
# 4
#   2
#     1
#     3
#   5

# 输入样例 2：
# 5 4 4 3 3 7 8 10

# 输出样例 2：
# 5
#   4
#     3
#   7
#     8
#       10

class BST(object):
	def __init__(self, key, height=0, left=None, right=None):
		self.left = left
		self.right = right
		self.label = key
		self.height = height

def bst_add(tree, key, height=0):
	if tree is None:
		return BST(key, height)
	if key < tree.label:
		tree.left = bst_add(tree.left, key, height+1)
	elif key > tree.label:
		tree.right = bst_add(tree.right, key, height+1)
	return tree

def preorder(x):
	if x is None:
		return
	print(2*x.height*" " + str(x.label))
	preorder(x.left)
	preorder(x.right)

if __name__ == '__main__':
	tree = None
	nums = input().split(' ')

	for num in nums:
		tree = bst_add(tree, int(num))

	preorder(tree)
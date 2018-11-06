# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-23 22:22:40

# 描述
# 给定两组数字，分别生成两棵二叉搜索树，将两棵树进行合并，相同节点位置的数字相加，如果某个节点位置其中一棵树有节点而另一棵树没有节点，则该节点位置直接生成为有数据的节点。
# 如下两棵树：
# 1
#  \
#   3
#  / \
# 2   5
#
#   2
#  / \
# 1   3
#      \
#       4
#        \
#         7
# 合并后的结果如下：
#   3
#  / \
# 1   6
#    / \
#   2   9
#        \
#         7
# 注意：合并后的树不一定是二叉搜索树，不用重新排列各节点的位置。

# 输入
# 一共两行数据，每行一组数，用空格隔开。
# 按顺序生成两棵二叉搜索树。每棵树最多30000个节点。

# 输出
# 一行数据，合并后树的前序遍历结果，用空格隔开各个数字。

# 输入样例：
# 1 3 2 5
# 2 1 3 4 7

# 输出样例：
# 3 1 6 2 9 7

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

def bst_combine(tree_1, tree_2):
	tree_1.label += tree_2.label

	if tree_2.left is not None:
		if tree_1.left is None:
			tree_1.left = BST(0)
		bst_combine(tree_1.left, tree_2.left)

	if tree_2.right is not None:
		if tree_1.right is None:
			tree_1.right = BST(0)
		bst_combine(tree_1.right, tree_2.right)

def preorder(x, answer):
	if x is None:
		return
	answer.append(str(x.label))
	preorder(x.left, answer)
	preorder(x.right, answer)

if __name__ == '__main__':
	tree_1 = None
	tree_2 = None
	answer = []
	nums_1 = input().split(' ')
	nums_2 = input().split(' ')

	for num in nums_1:
		tree_1 = bst_add(tree_1, int(num))
	for num in nums_2:
		tree_2 = bst_add(tree_2, int(num))

	bst_combine(tree_1, tree_2)
	preorder(tree_1, answer)
	print(" ".join(answer))
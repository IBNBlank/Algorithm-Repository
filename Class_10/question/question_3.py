# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-23 22:18:56

# 描述
# 给定一组数字，按顺序生成一颗二叉搜索树，然后给定一个数字sum，请问是否能找到从根节点开始走到某个节点的一条路径，其经过的节点数字之和为sum。
# 例如下面的二叉搜索树：
#     4
#    / \
#   2   5
#  / \
# 1   3
# sum 为 9，则4->2->3之和为9，应该输出True。

# 输入
# 第一行为一组数字，用空格隔开，最多有100000个数字。
# 第二行有一个数字sum。

# 输出
# 输出True或者False

# 输入样例：
# 30 40 50 35 20 10 60 55 70 25
# 70

# 输出样例：
# True

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

def answer(x, sum_left):
	if sum_left == 0:
		return True
	if x is None:
		return False
	return answer(x.left, sum_left-x.label) or answer(x.right, sum_left-x.label)

if __name__ == '__main__':
	tree = None
	nums = input().split(' ')
	sum_left = int(input())

	for num in nums:
		tree = bst_add(tree, int(num))

	print(answer(tree, sum_left))
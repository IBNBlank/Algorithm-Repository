# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-17 12:46:57
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-27 20:43:31

class BST(object):
	def __init__(self, key):
		self.left = None
		self.right = None
		self.label = key

def bst_add(tree, x):
	if tree is None:
		return BST(x)
	if x < tree.label:
		tree.left = bst_add(tree.left, x)
	elif x > tree.label:
		tree.right = bst_add(tree.right, x)
	return tree

def find_path_sum(x, remain_sum):
	if remain_sum == 0:
		return True
	if x is None or remain_sum < 0:
		return False
	return find_path_sum(x.left, remain_sum - x.label) or find_path_sum(x.right, remain_sum - x.label)

s = input()
# s = '30 40 50 35 20 10 60 55 70 25'
# s = '0 1 7 10 1'
s_list = s.split(' ')
int_list = [int(i) for i in s_list]

s = input()
# s = '70'
# s = '0 10'
path_sum = int(s)

bst = BST(int_list[0])
for i in int_list[1:]:
	bst = bst_add(bst, i)

print(find_path_sum(bst, path_sum))
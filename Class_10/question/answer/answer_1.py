# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-17 12:46:57
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-27 20:42:28

class BST(object):
	def __init__(self, key):
		self.left = None
		self.right = None
		self.label = key

def bst_add(tree, x):
	if tree is None:
		return BST(x)
	if x<tree.label:
		tree.left = bst_add(tree.left, x)
	elif x>tree.label:
		tree.right = bst_add(tree.right, x)
	return tree

def preorder_tree_print(x, level):
	if x is None:
		return
	print('  ' * level + str(x.label))
	preorder_tree_print(x.left, level + 1)
	preorder_tree_print(x.right, level + 1)

s = input()
s_list = s.split(' ')
int_list = [int(i) for i in s_list]
bst = BST(int_list[0])
for i in int_list[1:]:
	bst = bst_add(bst, i)
preorder_tree_print(bst, 0)
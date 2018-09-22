# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:15:51
class BST(object):
	def __init__(self, key):
		self.left = None
		self.right = None
		self.label = key

def bst_add(tree, x):
	height = 0
	if tree is None:
		return (BST(x), 1)
	if x<tree.label:
		tree.left, height = bst_add(tree.left, x)
		height += 1
	elif x>tree.label:
		tree.right, height = bst_add(tree.right, x)
		height += 1
	return (tree, height)

s = input()
s_list = s.split(' ')
bst = BST(int(s_list[0]))
max_height = 1
for item in s_list[1:]:
	_, height = bst_add(bst, int(item))
	if height>max_height:
		max_height = height
print(max_height)
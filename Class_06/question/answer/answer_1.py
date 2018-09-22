# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:16:13
class BST(object):
	def __init__(self, key):
		self.left = left
		self.right = right
		self.label = key

def bst_add(tree, x):
	if tree is None:
		return (BST(x), True)
	flag = False
	if x<tree.label:
		tree.left, flag = bst_add(tree.left, x)
	elif x>tree.label:
		tree.right, flag = bst_add(tree.right, x)
	return (tree, flag)

s = input()
s_list = s.split(' ')
bst = BST(s_list[0])
count = 1
for item in s_list[1:]:
	bst, flag = bst_add(bst, item)
	if flag:
		count += 1
print(count)
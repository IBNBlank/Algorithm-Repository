# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:15:38
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

s = input()
s_list = s.split(' ')
bst = BST(int(s_list[0]))
for item in s_list[1:]:
	bst_add(bst, int(item))
path = []
node = bst
while node:
	path.append(str(node.label))
	node = node.right
print('->'.join(path))
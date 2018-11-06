# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-17 12:46:57
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-27 20:43:45

global merged_tree_preorder_list
merged_tree_preorder_list = []

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

def preorder(x):
	global merged_tree_preorder_list
	if x is None:
		return
	merged_tree_preorder_list.append(str(x.label))
	preorder(x.left)
	preorder(x.right)

def preorder_merge(t1, t2):
	if t1 is None and t2 is None:
		return None
	elif t1 is None and t2 is not None:
		return t2
	elif t1 is not None and t2 is None:
		return t1
	else:
		merged_tree = BST(t1.label + t2.label)
		merged_tree.left = preorder_merge(t1.left, t2.left)
		merged_tree.right = preorder_merge(t1.right, t2.right)
		return merged_tree

s = input()
# s = '1 3 2 5'
s_list = s.split(' ')
node_list1 = [int(i) for i in s_list]

s = input()
# s = '2 1 3 4 7'
s_list = s.split(' ')
node_list2 = [int(i) for i in s_list]

bst1 = BST(node_list1[0])
for i in node_list1[1:]:
	bst1 = bst_add(bst1, i)

bst2 = BST(node_list2[0])
for i in node_list2[1:]:
	bst2 = bst_add(bst2, i)

merged_tree = preorder_merge(bst1, bst2)
preorder(merged_tree)
print(' '.join(merged_tree_preorder_list))
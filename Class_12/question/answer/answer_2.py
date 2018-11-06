# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-17 12:46:57
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-27 20:42:49

class BST(object):
	def __init__(self, key, l):
		self.parent = None
		self.left = None
		self.right = None
		self.level = l
		self.label = key

def bst_add(tree, x, l):
	if tree is None:
		return BST(x, l)
	if x < tree.label:
		tree.left = bst_add(tree.left, x, l + 1)
		tree.left.parent = tree
	elif x > tree.label:
		tree.right = bst_add(tree.right, x, l + 1)
		tree.right.parent = tree
	return tree

def bst_find(tree, search_key):
	if tree is None:
		return None
	if search_key == tree.label:
		return tree
	elif search_key < tree.label:
		return bst_find(tree.left, search_key)
	else:
		return bst_find(tree.right, search_key)

def find_path(x, min_item, max_item):
	pl = bst_find(x, min_item)
	pr = bst_find(x, max_item)

	l_path = []
	r_path = []

	while pl.label != pr.label:
		if pl.level < pr.level:
			if pr.parent is not None:
				r_path.insert(0, pr.label)
				pr = pr.parent
		elif pr.level < pl.level:
			if pl.parent is not None:
				l_path.append(pl.label)
				pl = pl.parent
		else:
			r_path.insert(0, pr.label)
			pr = pr.parent
			l_path.append(pl.label)
			pl = pl.parent

	l_path.append(pl.label)
	final_path = l_path + r_path
	final_path = [str(i) for i in final_path]
	print('->'.join(final_path))

s = input()
# s = '30 40 50 35 20 10 60 55 70 25'
# s = '0 1 7 10 1'
s_list = s.split(' ')
int_list = [int(i) for i in s_list]

s = input()
# s = '35 55'
# s = '0 10'
min_item, max_item = s.split(' ')
min_item = int(min_item)
max_item = int(max_item)

min_added = False
max_added = False

bst = BST(int_list[0], 0)
for i in int_list[1:]:
	# 非常简单的剪枝，如果最大节点和最小节点都已经加到二叉树里了
	# 那么剩下的节点就不用再加进来了
	if not min_added or not max_added:
		bst = bst_add(bst, i, 0)
	if i == min_item:
		min_added = True
	if i == max_item:
		max_added = True

find_path(bst, min_item, max_item)
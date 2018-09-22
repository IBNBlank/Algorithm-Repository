# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-19 00:59:34

class BST(object):
	def __init__(self, key, left=None, right=None):
		self.left = left
		self.right = right
		self.label = key

def bst_find(tree, key):
	if tree is None:
		return None
	if key == tree.label:
		return tree
	elif key < tree.label:
		return bst_find(tree.left, key)
	elif key > tree.label:
		return bst_find(tree.right, key)

def bst_add(tree, key):
	if tree is None:
		return BST(key)
	if key < tree.label:
		tree.left = bst_add(tree.left, key)
	elif key > tree.label:
		tree.right = bst_add(tree.right, key)
	return tree

def bst_leftest(tree):
	while tree.left is not None:
		tree = tree.left
	return tree

def bst_delete(tree, key):
	if tree is None:
		return None
	if tree.label > key:
		tree.left = bst_delete(tree.left, key)
		return tree
	elif tree.label < key:
		tree.right = bst_delete(tree.right, key)
		return tree
	else:
		if tree.left is None and tree.right is None:
			return None
		elif tree.left is None:
			return tree.right
		elif tree.right is None:
			return tree.left
		else:
			temp_tree = bst_leftest(tree.right)
			tree.label = temp_tree.label
			tree.right = bst_delete(tree.right, temp_tree.label)

def bst_size(tree):
	if tree is None:
		return 0
	else:
		return 1 + bst_size(tree.left) + bst_size(tree.right)

def bst_height(tree):
	if tree is None:
		return 0
	else:
		return 1 + max(bst_height(tree.left), bst_height(tree.right))

if __name__ == '__main__':
	tree = None
	nums = input().split(" ")
	for num in nums:
		tree = bst_add(tree, int(num))
	print(bst_size(tree))

	tree = bst_delete(tree, 5)
	print(bst_size(tree))

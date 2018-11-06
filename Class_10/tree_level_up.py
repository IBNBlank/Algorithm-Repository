# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-23 19:17:39

###################
##### 树的遍历 #####
###################

##### 深度优先遍历 #####

### 前序 ###
def preorder(x):
	if x is None:
		return
	print(x.label)
	preorder(x.left)
	preorder(x.right)

### 中序 ###
def inorder_small_to_big(x):
	if x is None:
		return
	inorder_small_to_big(x.left)
	print(x.label)
	inorder_small_to_big(x.right)

def inorder_big_to_small(x):
	if x is None:
		return
	inorder_big_to_small(x.right)
	print(x.label)
	inorder_big_to_small(x.left)

### 后序 ###
def postorder(x):
	if x is None:
		return
	postorder(x.left)
	postorder(x.right)
	print(x.label)

##### 层序遍历 #####

### 迭代加深 ###
def levelorder(x):
	for i in range(x.height):
		visit_level(x, i)

def visit_level(x, i):
	if x in None:
		return
	if i == 0:
		print(x.label)
	else:
		visit_level(x.left, i-1)
		visit_level(x.right, i-1)

### 中序 ###
def inorder_small_to_big(x):
	if x is None:
		return
	preorder(x.left)
	print(x.label)
	preorder(x.right)

def inorder_big_to_small(x):
	if x is None:
		return
	preorder(x.right)
	print(x.label)
	preorder(x.left)

### 后序 ###
def preorder(x):
	if x is None:
		return
	preorder(x.left)
	preorder(x.right)
	print(x.label)

###################
##### 树的搜索 #####
###################

##### 剪枝 #####

#################
##### 空间树 #####
#################
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-23 22:17:05

# 描述
# 给定一组数字，按顺序生成一颗二叉搜索树，然后给定两个数字a和b，分别为二叉树中的两个节点数字，找到从a节点到b节点的一条路径。
# 例如下面的二叉搜索树：
#     4
#    / \
#   2   5
#  / \
# 1   3
# 从3到5的路径为3->2->4->5

# 输入
# 第一行为一组数字，用空格隔开，最多有100000个数字。
# 第二行有两个数字a和b，都代表了某个节点的数字，且a<=b。

# 输出
# 输出从a节点到b节点的路径，节点数字间用->连接。

# 输入样例 1：
# 30 40 50 35 20 10 60 55 70 25
# 35 55

# 输出样例 1：
# 35->40->50->60->55

# 输入样例 2：
# 0 1 7 10 1
# 0 10

# 输出样例 2：
# 0->1->7->10

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

def bst_find(tree, key, way_list, judge, flag):
	if tree is None:
		return
	if key == judge:
		way_list = [tree.label]
		flag = True
	else:
		way_list.append(tree.label)
	if key < tree.label:
		bst_find(tree.left, key, way_list, judge, flag)
	elif key > tree.label:
		bst_find(tree.right, key, way_list, judge, flag)

def output_answer(small_list, big_list):
	final_list = []
	length = min(len(small_list), len(big_list))

	for i in range(length):
		if small_list[i] in big_list:
			key = i

	small_list = small_list[key:]
	small_list.reverse()
	small_list.pop()
	big_list = big_list[key:]

	final_list = small_list + big_list
	strs = [ str(x) for x in final_list ]
	print("->".join(strs))

if __name__ == '__main__':
	tree = None
	small_list = []
	big_list = []
	over_flag = False

	nums = input().split(' ')
	small, big = input().split(' ')
	small = int(small)
	big = int(big)

	for num in nums:
		tree = bst_add(tree, int(num))

	bst_find(tree, small, small_list, big, over_flag)
	if over_flag:
		small_list.reverse()
		strs = [ str(x) for x in small_list ]
		print("->".join(strs))
	else:
		bst_find(tree, big, big_list, small, over_flag)
		if over_flag:
			strs = [ str(x) for x in big_list ]
			print("->".join(strs))
		else:
			output_answer(small_list, big_list)
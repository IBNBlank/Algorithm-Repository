# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 16:20:59

# 描述
# 利用2-3树结构实现一个集合，输出集合中元素的个数

# 输入
# 一行数据，包含多个数字，数字之间用空格隔开，最多有60000个数字。

# 输出
# 一个数字，集合里有多少个不重复的元素。

# 输入样例：
# 1 2 3 4 1 4 0 4 1 5

# 输出样例：
# 6

##### QUESTION 1 #####
class Node(object):
	def __init__(self, key_1, key_2=None, left=None, middle=None, right=None):
		self.key_1 = key_1
		self.key_2 = key_2
		self.left = left
		self.middle = middle
		self.right = right

class Tree23(object):
	def __init__(self):
		self.__root = None
		self.__size = 0

	def tree_add(self):
		pass

	def tree_size(self):
		return self.__size





if __name__ == '__main__':
	tree = None
	nums = input().split(" ")
	for num in nums:
		tree = bst_add(tree, int(num))
	print(bst_size(tree))

	tree = bst_delete(tree, 5)
	print(bst_size(tree))

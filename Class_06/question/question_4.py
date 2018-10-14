# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   Administrator
# @Last Modified time: 2018-10-01 23:38:03

# 描述
# 如果A，B是C的父母亲，则A，B是C的parent，C是A，B的child，
# 如果A，B是C的（外）祖父，祖母，则A，B是C的grandparent，C是A，B的grandchild，
# 如果A，B是C的（外）曾祖父，曾祖母，则A，B是C的great-grandparent，C是A，B的great-grandchild，
# 之后再多一辈，则在关系上加一个great-。

# 输入
# 首先包含2个整数n（0<=n<=26）和m（0<m<50）, 分别表示有n个亲属关系和m个问题,
# 然后接下来是n行的形式如ABC的字符串，表示A的父母亲分别是B和C，
# 如果A的父母亲信息不全，则用-代替，例如A-C,
# 再然后是m行形式如FA的字符串,表示询问F和A的关系，F是A的什么人。

# 输出
# 如果询问的2个人是直系亲属，请按题目描述输出2者的关系，如果没有直系关系，请输出-。
# 具体含义和输出格式参见样例.

# 输入样例：
# 3 3
# ABC
# EFG
# CDE
# BE
# AF
# FA

# 输出样例：
# -
# great-grandchild
# great-grandparent

########################
### 解决不了多父母情况 ###
########################

ASCII_A = ord("A")
answers = []

class Child(object):
	def __init__(self, parent_1=None, parent_2=None):
		self.parent_1 = parent_1
		self.parent_2 = parent_2

def relationship_add(child_list, s):
	global ASCII_A

	child_no = ord(s[0]) - ASCII_A
	parent_1_no = ord(s[1]) - ASCII_A
	parent_2_no = ord(s[2]) - ASCII_A

	if child_no == parent_1_no or child_no == parent_2_no:
		return
	elif parent_1_no == parent_2_no:
		parent_2_no = ord("-") - ASCII_A

	if parent_1_no >= 0:
		child_list[child_no].parent_1 = child_list[parent_1_no]

	if parent_2_no >= 0:
		child_list[child_no].parent_2 = child_list[parent_2_no]

def relationship_find(child_list, s):
	global ASCII_A
	global answers

	child_1 = child_list[ord(s[0])-ASCII_A]
	child_2 = child_list[ord(s[1])-ASCII_A]

	if child_1 == child_2:
		answers.append("-")
	else:
		code = parent_find(child_1, child_2, 0)
		if code > 0:
			if code == 1:
				answers.append("child")
			else:
				answers.append("great-"*(code-2) + "grandchild")
			return
		code = parent_find(child_2, child_1, 0)
		if code > 0:
			if code == 1:
				answers.append("parent")
			else:
				answers.append("great-"*(code-2) + "grandparent")
		else:
			answers.append("-")

def parent_find(child, parent, count):
	if count > 30 or (child.parent_1 == None and child.parent_2 == None):
		return -100
	elif child.parent_1 == parent or child.parent_2 == parent:
		return 1
	else:
		if child.parent_1 != None:
			code = 1 + parent_find(child.parent_1, parent, count+1)
			if code > 0:
				return code
		if child.parent_2 != None:
			code = 1 + parent_find(child.parent_2, parent, count+1)
			return code
		else:
			return -100

if __name__ == '__main__':
	child_list = []
	for _ in range(26):
		child_list.append(Child())

	m, n = input().split(" ")
	for _ in range(int(m)):
		s = input()
		relationship_add(child_list, s)
	for _ in range(int(n)):
		s = input()
		relationship_find(child_list, s)

	for answer in answers:
		print(answer)
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-13 00:04:08
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-17 12:48:27

# 描述：
# 给定一组数字，将他们用链表的形式进行存储。另外再给一个数字，将它插入到链表的末尾。输出这个链表。

# 输入：
# 给定一组数字，将他们用链表的形式进行存储。另外再给一个数字，将它插入到链表的末尾。输出这个链表。
# 第二行是一个数字。
# 数字均在int范围内。

# 输出：
# 一行输出，数字之间用“->”来表示链表方向。比如：1->2->3->4

# 输入样例：
# 1 2 3
# 4

# 输出样例：
# 1->2->3->4

##### QUESTION 2 #####
class IntNode(object):
	def __init__(self, i, n):
		self.item = i
		self.next = n

class SLList(object):
	def __init__(self):
		self.__first = IntNode(None, None)
		self.__last = self.__first

	def add(self, x):
		temp = self.__last
		self.__last = IntNode(x, None)
		temp.next = self.__last

	def get_all(self):
		out_str = ""
		p = self.__first.next
		while p is not None:
			out_str += "{}->".format(p.item)
			p = p.next
		print(out_str[:-2])

if __name__ == '__main__':
	l = SLList()
	nums = input().split(' ')
	nums.append(input())

	for num in nums:
		l.add(num)

	l.get_all()
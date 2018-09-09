# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-13 00:04:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-17 12:57:33

# 描述：
# 给定一个单向链表，要求将第m位到第n位（从0开始编号位数）的元素翻转过来。
# 注1：m和n一定都在链表长度内
# 注2：待翻转的元素包括第m和n位

# 输入：
# 两行数据
# 第一行为链表元素，用空格隔开各个元素
# 第二行有两个数字，分别是m和n
# 注：链表元素个数最大为1000

# 输出：
# 翻转后的链表结果
# 元素之间用->表示连接方向

# 输入样例 1：
# 1 2 3 4 5 6 7
# 2 5

# 输出样例 1：
# 1->2->6->5->4->3->7

# 输入样例 2：
# 1 2 3 4 5 6 7
# 0 1

# 输出样例 2：
# 2->1->3->4->5->6->7

##### QUESTION 3 #####
class IntNode(object):
	def __init__(self, i, n):
		self.item = i
		self.next = n

class SLList(object):
	def __init__(self):
		self.__first = IntNode(None, None)
		self.__last = self.__first
		self.__size = 0

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

	def reverse(self, order_1, order_2):
		p1 = self.__first
		p2 = None
		pt = None
		pt1 = None
		pt2 = None
		for i in range(order_1):
			p1 = p1.next
		p2 = p1
		for i in range(order_2-order_1+2):
			p2 = p2.next
		pt = p1
		pt1 = p1
		pt2 = p1.next
		while pt2 is not p2:
			pt = pt2
			pt2 = pt2.next
			pt.next = pt1
			pt1 = pt
		temp = p1.next
		p1.next = pt
		temp.next = p2

if __name__ == '__main__':
	l = SLList()
	nums = input().split(' ')
	orders = input().split(' ')
	order_1 = int(orders[0])
	order_2 = int(orders[1])

	if order_1 > order_2:
		temp = order_1
		order_1 = order_2
		order_2 = temp

	for num in nums:
		l.add(num)

	l.reverse(order_1, order_2)
	l.get_all()
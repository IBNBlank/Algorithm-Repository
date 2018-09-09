# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 21:09:10
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:19:01

# 描述：
# 给定一个链表和链表中的一个位置m，在这个位置的后面插入一个新的元素x。

# 输入：
# 一共有两行，第一行是多个数字，以空格隔开，最多100000个数字。
# 第二行是两个个数字，第一个数字是m，第二个是x。
# 数字均在int范围内。

# 输出：
# 一行输出，数字之间用“->”来表示链表方向。比如：1->2->3->4

# 输入样例 1：
# 1 2 3 4
# 0 1

# 输出样例 1：
# 1->1->2->3->4

# 输入样例 2：
# 3 4 5 6 7 8
# 2 10

# 输出样例 2：
# 3->4->5->10->6->7->8

class IntNode(object):
	def __init__(self, i, n):
		self.item = i
		self.next = n

class SLList(object):
	def __init__(self):
		self.__sentinel = IntNode(None, None)
		self.__last = self.__sentinel

	def add(self, x):
		temp = self.__last
		self.__last = IntNode(x, None)
		temp.next = self.__last

	def add_chosen(self, order, value):
		prev = self.__sentinel
		for i in range(order+1):
			prev = prev.next
		prev.next = IntNode(value, prev.next)

	def get_all(self):
		out_str = ""
		p = self.__sentinel.next
		while p is not None:
			out_str += "{}->".format(p.item)
			p = p.next
		print(out_str[:-2])

if __name__ == '__main__':
	l = SLList()
	nums = input().split(' ')
	order, value = input().split(' ')

	for num in nums:
		l.add(num)

	l.add_chosen(int(order), value)

	l.get_all()
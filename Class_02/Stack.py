# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 20:33:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-20 12:22:59
class Stack(object):
	def __init__(self, data=[]):
		self.__data = data

	def push(self, x):
		self.__data.append(x)

	def pop(self):
		return self.__data.pop()

if __name__ == '__main__':
	Stack_test = Stack()

	Stack_test.push(0)
	Stack_test.push(1)
	Stack_test.push(2)
	Stack_test.push(3)
	Stack_test.push(4)

	print(Stack_test.pop())
	print(Stack_test.pop())
	print(Stack_test.pop())
	print(Stack_test.pop())
	print(Stack_test.pop())
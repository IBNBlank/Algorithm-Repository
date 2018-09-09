# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 20:42:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-20 16:12:29

class MySet(object):
	def __init__(self, data=[]):
		self.__data = []
		for item in data:
			if item not in self.__data:
				self.__data.append(item)

	def add_element(self, item):
		if item not in self.__data:
			self.__data.append(item)

	def get_all(self):
		return self.__data

if __name__ == '__main__':
	Set_test = MySet([1, 2, 3, 4, 5, 2, 3, 4, 5])
	print(Set_test.get_all())

	Set_test.add_element(1)
	print(Set_test.get_all())
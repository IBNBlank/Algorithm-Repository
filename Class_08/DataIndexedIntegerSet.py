# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-03 23:03:57

class DataIndexedIntegerSet(object):
	"""DataIndexedIntegerSets can store integers
	between 0 and 15."""
	def __init__(self):
		self.__present = [False] * 16

	def add(self, i):
		self.__present[i] = True

	def contains(self, i):
		return self.__present[i]

if __name__ == '__main__':
	diis = DataIndexedIntegerSet()
	print(diis.contains(5))
	diis.add(5)
	print(diis.contains(5))
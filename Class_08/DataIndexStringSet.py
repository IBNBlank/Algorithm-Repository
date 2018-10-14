# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-10-03 23:28:21
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-03 23:31:25

def string_to_int(s):
	"""Converts the string s into an integer by 
	multiplying each character by a power of 126 
	and adding them. bee --> 1568675"""
	int_rep = 0
	for c in s:
		int_rep *= 126
		int_rep += ord(c)
	return int_rep

class DataIndexStringSet(object):
	def __init__(self):
		self.__present = [False] * 10000000

	def add(self, s):
		int_rep = string_to_int(s)
		self.__present[int_rep] = True

	def contains(self, s):
		int_rep = string_to_int(s)
		return self.__present[int_rep]

if __name__ == '__main__':
	diss = DataIndexStringSet()
	print(diss.contains("bee"))
	diss.add("bee")
	print(diss.contains("bee"))
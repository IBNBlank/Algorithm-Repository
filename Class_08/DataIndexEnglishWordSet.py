# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-10-03 23:10:44
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-03 23:25:22

def letter_num(c):
	"""Takes a character and returns the letter 
	corresponding to that character. a --> 1, 
	b --> 2, c --> 3, ..., z --> 26"""
	return ord(c) - 96

def english_to_int(s):
	"""Converts the string s into an integer by 
	multiplying each character by a power of 27 
	and adding them. bee --> 1598"""
	int_rep = 0
	for c in s:
		int_rep *= 27
		int_rep += letter_num(c)
	return int_rep

class DataIndexEnglishWordSet(object):
	def __init__(self):
		self.__present = [False] * 10000000

	def add(self, w):
		int_rep = english_to_int(w)
		self.__present[int_rep] = True

	def contains(self, w):
		int_rep = english_to_int(w)
		return self.__present[int_rep]

if __name__ == '__main__':
	diews = DataIndexEnglishWordSet()
	print(diews.contains("bee"))
	diews.add("bee")
	print(diews.contains("bee"))
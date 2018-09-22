# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 11:15:19
class DS(object):
	def __init__(self, N):
		self.__id = list(range(0, N))

	def is_connected(self, parent, child):
		pid = ord(parent) - ord('A')
		cid = ord(child) - ord('A')

		connected = False
		generation_count = 0
		while not connected:
			generation_count += 1
			pid = self.__id[pid]
			if pid == cid:
				connected = True
			elif pid == self.__id[pid]:
				break

		if connected:
			result = 'child'
			if generation_count > 1:
				result = 'grandchild'
			if generation_count > 2:
				for _ in range(2, generation_count):
					result = 'great-' + result
			return result
		else:
			return '-'

	def connect(self, parent, child):
		if parent != '-':
			self.__id[ord(parent)-ord('A')] = ord(child)-ord('A')

s = input()
n, m = s.split(' ')
n = int(n)
m = int(m)
ds = DS(26)
for _ in range(n):
	child, father, mother = input()
	ds.connect(father, child)
	ds.connect(mother, child)
for _ in range(m):
	a, b = input()
	if a == b:
		print('-')
	else:
		result = ds.is_connected(b, a)
		if result == '-':
			result = ds.is_connected(a, b)
			result = result.replace('child', 'parent')
		print(result)
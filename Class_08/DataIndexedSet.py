# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-10-05 01:01:19
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-08 21:55:54

class DataIndexedSet(object):
	def __init__(self):
		self.__size = 0
		self.__buckets = 4
		self.__limit = 1.5
		self.__buckets_list = [[] for i in range(self.__buckets)]

	def add(self, item):
		if item is None:
			return

		hash_value = hash(item)
		hash_bucket = hash_value % self.__buckets

		if hash_value not in self.__buckets_list[hash_bucket]:
			self.__buckets_list[hash_bucket].append(hash_value)
			self.__size += 1

		self.__resize()

	def __resize(self):
		if self.__size/self.__buckets > self.__limit:
			old_buckets_num = self.__buckets
			self.__buckets_list.extend([[] for i in range(self.__buckets)])
			self.__buckets *= 2
			for bucket in self.__buckets_list[:old_buckets_num]:
				remain_num = len(bucket)
				for i in range(remain_num):
					hash_value = hash(bucket[i])
					hash_bucket = hash_value % self.__buckets
					self.__buckets_list[hash_bucket].append(hash_value)
				del bucket[:remain_num]

	def contains(self, item):
		hash_value = hash(item)
		hash_bucket = hash_value % self.__buckets

		return hash_value in self.__buckets_list[hash_bucket]

if __name__ == '__main__':
	dis = DataIndexedSet()
	print(dis.contains(1))
	print(dis.contains(2))
	print(dis.contains(3))
	print(dis.contains(4))
	print(dis.contains(5))
	print(dis.contains(6))
	print(dis.contains(7))
	print(dis.contains(8))
	print(dis.contains(9))
	print(dis.contains(0))
	dis.add(1)
	dis.add(2)
	dis.add(3)
	dis.add(4)
	dis.add(5)
	dis.add(6)
	dis.add(7)
	dis.add(8)
	dis.add(9)
	dis.add(0)
	print(dis.contains(1))
	print(dis.contains(2))
	print(dis.contains(3))
	print(dis.contains(4))
	print(dis.contains(5))
	print(dis.contains(6))
	print(dis.contains(7))
	print(dis.contains(8))
	print(dis.contains(9))
	print(dis.contains(0))
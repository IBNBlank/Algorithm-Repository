# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 16:24:09

# 描述
# 根据课上内容设计哈希表结构。
# 给定一组数据，以哈希表的方式进行存储，并判断另一组给定数据是否存在于哈希表中。
# 哈希码可以直接用python的hash()函数来获取。
# 每个bucket采用前面学的链表来存储。
# 别忘了实现课上所说的resize()方法。

# 输入
# 第一行数字n，表示接下来有多少行数据。
# 第二行到第n+1行，每行一个数据，需要添加到哈希表里。
# 第n+2行数字m，表示接下来多少行数据。
# 接下来m行，每行一个数据，需要判断是否存在于前面的哈希表中。

# 输出
# m行数据，每行输出True或者False。

# 输入样例：
# 3
# 1
# 3
# 5
# 2
# 1
# 2

# 输出样例：
# True
# False

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
	add_nums = []
	contains_nums = []
	n = int(input())
	for _ in range(n):
		add_nums.append(int(input()))
	m = int(input())
	for _ in range(m):
		contains_nums.append(int(input()))
	dis = DataIndexedSet()
	for num in add_nums:
		dis.add(num)
	for num in contains_nums:
		print(dis.contains(num))
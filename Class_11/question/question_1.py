# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:45:20

# 描述
# 有N个学生的数据，将学生数据按成绩高低排序，如果成绩相同则按姓名字符的字母序排序，
# 如果姓名的字母序也相同则按照学生的年龄排序，并输出N个学生排序后的信息。
# 不可以用系统自带的sort()方法。

# 输入
# 第一行有一个整数N（N<=8000），接下来的N行包括N个学生的数据。
# 每个学生的数据包括姓名（长度不超过10的字符串）、年龄（整形数）、成绩（小于等于100的正数）。

# 输出
# 将学生信息按成绩进行排序，成绩相同的则按姓名的字母序进行排序。
# 然后输出学生信息，按照如下格式：
# 姓名 年龄 成绩

# 输入样例 1：
# 3
# zhao 19 90
# qian 20 90
# sun 19 100

# 输出样例 1：
# qian 20 90
# zhao 19 90
# sun 19 100

class Student(object):
	def __init__(self, arg):
		self.name = arg[0]
		self.age = arg[1]
		self.grade = arg[2]

	def __lt__(self, student):
		return smaller(self, student)

	def __eq__(self, student):
		return (self.name == student.name) and (self.age == student.age) and (self.grade == student.grade)

	def __str__(self):
		return "{} {} {}".format(self.name, self.age, self.grade)

def smaller(student_1, student_2):
	if student_1.grade < student_2.grade:
		return True
	elif student_1.grade == student_2.grade:
		if name_compare(student_1.name, student_2.name) == "<":
			return True
		elif name_compare(student_1.name, student_2.name) == "=":
			if student_1.age < student_2.age:
				return True

def name_compare(name_1, name_2):
	length = min(len(name_1), len(name_2))
	for i in range(length):
		if ord(name_1[i]) < ord(name_2[i]):
			return "<"
		elif ord(name_1[i]) > ord(name_2[i]):
			return ">"
	if len(name_1) == len(name_2):
		return "="
	elif len(name_1) < len(name_2):
		return "<"
	else:
		return ">"

class PriorityQueue(object):
	def __init__(self):
		self.__queue = [None]
		self.__size = 0

	def get_smallest(self):
		return self.__queue[1]

	def get_size(self):
		return self.__size

	def add(self, i):
		self.__size += 1
		self.__queue.append(i)
		self.__swim(self.__size)

	def remove_smallest(self):
		if self.__size > 1:
			self.__size -= 1
			data = self.__queue.pop()
			self.__queue[1] = data
			self.__sink(1)
		elif self.__size == 1:
			self.__size -= 1
			self.__queue.pop()

	def __swim(self, index):
		if index > 1:
			parent_index = self.__parent(index)
			if self.__queue[parent_index] > self.__queue[index]:
				self.__swap(index, parent_index)
				self.__swim(parent_index)

	def __sink(self, index):
		child = self.__left_child(index)
		if child > self.__size:
			return
		elif child == self.__size:
			if self.__queue[index] > self.__queue[child]:
				self.__swap(index, child)
		else:
			if self.__queue[child] > self.__queue[child+1]:
				child += 1
			if self.__queue[index] > self.__queue[child]:
				self.__swap(index, child)
				self.__sink(child)

	def __swap(self, index_1, index_2):
		self.__queue[index_1], self.__queue[index_2] = self.__queue[index_2], self.__queue[index_1]

	def __left_child(self, index):
		return index * 2

	def __right_child(self, index):
		return index * 2 + 1

	def __parent(self, index):
		return index // 2

if __name__ == '__main__':
	pq = PriorityQueue()

	num = int(input())
	for _ in range(num):
		student = input().split(" ")
		student[1] = int(student[1])
		student[2] = int(student[2])
		pq.add(Student(student))

	for _ in range(num):
		student = pq.get_smallest()
		print(student)
		pq.remove_smallest()
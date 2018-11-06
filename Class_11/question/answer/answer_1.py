# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-25 14:22:44
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:49:26

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

	def __str__(self):
		return '{} {} {}'.format(self.name, self.age, self.score)

	def __lt__(self, sdt):
		if self.score == sdt.score:
			if self.name == sdt.name:
				return self.age < sdt.age
			else:
				return self.name < sdt.name
		else:
			return self.score < sdt.score

n = int(input())
students = []
for _ in range(n):
	s_input = input()
	s_list = s_input.split(' ')
	current_student = Student(s_list[0], int(s_list[1]), int(s_list[2]))
	inserted = False
	for index, student in enumerate(students):
		if current_student < student:
			students.insert(index, current_student)
			inserted = True
			break
	if not inserted:
		students.append(current_student)

for student in students:
	print(student)
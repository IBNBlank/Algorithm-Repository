# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 21:31:56
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:22:53

# 描述：
# B公司组织了一场七夕配对活动，单身的男女生可以来参加活动。
# 配对规则如下
# 1.所有参加活动的人都只排成一列，来参加活动的女生只会和排在队伍最后的男生配对。
# 2.如果女生来到现场没有可以配对的男生则活动失败。
# 3.如果最后有没有被领走的男生则活动也失败。
# 问题如下
# 给定到场参加活动人士顺序的性别，问活动能不能成功举办。

# 输入：
# 一行数据，到场人士顺序的性别。
# 如：mfmfmfmmff
# 字符长度不超过50个。

# 输出：
# True或者False表示活动能否成功举办。

# 输入样例 1：
# mfmfmf

# 输出样例 1：
# True

# 输入样例 2：
# mfmmfffm

# 输出样例 2：
# False

class Stack(object):
	def __init__(self, data=[]):
		self.__data = data

	def push(self, x):
		self.__data.append(x)

	def pop(self):
		return self.__data.pop()

if __name__ == '__main__':
	sexes = list(input())
	over_flag = False

	Sex_Stack = Stack(["bottom"])

	for sex in sexes:
		if sex == "m":
			Sex_Stack.push(sex)
		else:
			if Sex_Stack.pop() is not "m":
				print("False")
				over_flag = True
				break

	if over_flag is False:
		if Sex_Stack.pop() == "bottom":
			print("True")
		else:
			print("False")

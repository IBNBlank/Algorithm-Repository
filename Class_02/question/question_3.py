# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 21:53:45
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:25:26

# 描述：
# C公司模仿B公司组织了一场七夕配对活动，单身的男女生可以来参加活动。
# 为了让配对活动更加完善，本次活动还考虑了双方的性格，双方必须性格也一致才能完成配对。
# 本着女士优先的原则，来参加活动的女生可以直接配对，先到的男生必须先等待。而如果女生来到现场没有可以配对的男生则活动失败，如果最后有没有被领走的男生则活动也失败。
# 假设所有参加活动的人都只排成一列，来参加活动的女生只会和排在队伍最后的男生配对。
# 给定到场参加活动人士顺序的性别，问活动能不能成功举办。

# 输入：
# 一行数据，到场人士顺序的性别和性格，数据之间用空格隔开。
# 如：m1 f1 m2 f2 m3 f3 m3 m3 f4 f4
# 参加的人数不超过20万。

# 输出：
# True或者False表示活动能否成功举办。

# 输入样例 1：
# m1 m2 m3 f3 f2 f1

# 输出样例 1：
# True

# 输入样例 2：
# m2 m3 m3 f1 f2 f3

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
	sexes = input().split(' ')
	over_flag = False

	Sex_Stack = Stack(["bottom"])

	for sex in sexes:
		if sex[0] == "m":
			Sex_Stack.push(sex)
		else:
			if sex[1] != Sex_Stack.pop()[1]:
				print("False")
				over_flag = True
				break

	if over_flag is False:
		if Sex_Stack.pop() == "bottom":
			print("True")
		else:
			print("False")
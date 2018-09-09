# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-02 15:59:34

# 描述：
# 给定一个整数n，写出n的因式分解式子，如：
# 12=2*2*3
# 12=2*6
# 12=3*4
# 12=12

# 输入：
# 一个数字n，n最大不超过250000000000

# 输出：
# n的因式分解式子，要求不能有重复的分解方法，比如12=2*2*3和12=2*3*2是一样的分解方法。
# 输出时从因子数最多的方法开始输出，式子中的因子要从小到大排列。
# 注意要按照n=m1*m2*m3……的格式输出

# 输入样例 1：
# 12

# 输出样例 1：
# 12=2*2*3
# 12=2*6
# 12=3*4
# 12=12

# 输入样例 2：
# 100

# 输出样例 2：
# 100=2*2*5*5
# 100=2*2*25
# 100=2*5*10
# 100=2*50
# 100=4*5*5
# 100=4*25
# 100=5*20
# 100=10*10
# 100=100

#################################################
### while自加 与 for range() 在速度上有巨大差别 ###
#################################################

answer = []
str_head = ""

def factorization(num, min_num):
	global answer
	for i in range(min_num, int(num**0.5+1)):
	 	if num%i == 0:
	 		answer.append(i)
	 		factorization(num//i, i)
	 		answer.pop()
	answer.append(num)
	get_answer(answer)
	answer.pop()

def get_answer(answer):
	global str_head
	string = str_head + str(answer[0])
	for i in answer[1:]:
		string += "*{}".format(i)
	print(string)

if __name__ == '__main__':
	num = int(input())
	str_head += "{}=".format(num)

	factorization(num, 2)
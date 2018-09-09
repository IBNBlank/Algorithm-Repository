# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-28 00:17:58

#################################################
### while自加 与 for range() 在速度上有巨大差别 ###
#################################################

answer = []
final_answer = []
str_head = ""

def factorization(num, min_num):
	global answer
	global final_answer
	for i in range(min_num, int(num**0.5+1)):
	 	if num%i == 0:
	 		answer.append(i)
	 		factorization(num//i, i)
	 		answer.pop()
	answer.append(num)
	final_answer.append(get_answer(answer))
	answer.pop()

def get_answer(answer):
	global str_head
	string = str_head + str(answer[0])
	for i in answer[1:]:
		string += "*{}".format(i)
	return string

def get_final_answer(final_answer):
	for answer in final_answer:
		print(answer)

if __name__ == '__main__':
	num = int(input())
	str_head += "{}=".format(num)

	factorization(num, 2)
	get_final_answer(final_answer)
# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:31:30
s = input()

stack = []
can_match =True
for item in s:
	if item == 'm':
		stack.append('m')
	else:
		if len(stack)==0:
			can_match = False
			break
		else:
			stack.pop()
if len(stack)>0:
	can_match = False
print(can_match)
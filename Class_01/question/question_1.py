# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-15 15:19:33

# 描述：
# 输入A、B，输出A+B。

# 输入：
# 输入的第一行包括两个整数，由空格分隔，分别表示A、B。

# 输出：
# 输出一行，包括一个整数，表示A+B的值。A、B以及A+B的和均在Int范围内。

# 输入样例：
# 12 34

# 输出样例：
# 46

##### QUESTION 1 #####
nums = input().split(' ')
a = int(nums[0])
b = int(nums[1])
print(a+b)
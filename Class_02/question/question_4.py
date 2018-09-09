# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-19 22:22:05
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-22 16:28:43

# 描述：
# 一共两行数据，第一行是一共有多少人，第二行是每次可以有多少人来拍照。假设所有人的身高都正好各不相同。
# 总人数不超过20人，一次拍照最多不超过6人。

# 输入：
# 将所有可能排列的方式输出出来。
# 每行输出一个列表，列表内的数字为拍照时身高排列的序号，如：[10,9,8,7]。
# 例如，有20个人，那么身高最高的人编号就是20，最低的就是1。
# 输出时列表内的数字需要从大到小排列，列表内编号之和最大的排列方式要优先输出。

# 输出：
# True或者False表示活动能否成功举办。

# 输入样例 1：
# 5
# 2

# 输出样例 1：
# [5, 4]
# [5, 3]
# [5, 2]
# [5, 1]
# [4, 3]
# [4, 2]
# [4, 1]
# [3, 2]
# [3, 1]
# [2, 1]

# 输入样例 2：
# 4
# 3

# 输出样例 2：
# [4, 3, 2]
# [4, 3, 1]
# [4, 2, 1]
# [3, 2, 1]

def sub_list(nums, target, count, answer):
	if not nums or count >= target:
		if count == target:
			print(answer)
	else:
		num_temp = nums.pop()
		answer.append(num_temp)
		sub_list(nums, target, count+1, answer)
		answer.pop()
		sub_list(nums, target, count, answer)
		nums.append(num_temp)

if __name__ == '__main__':
	order = int(input())
	target = int(input())

	orders = list(range(1, order+1))
	answer = []

	sub_list(orders, target, 0, answer)
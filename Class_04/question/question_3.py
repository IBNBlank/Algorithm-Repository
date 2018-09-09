# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 07:22:24

# 描述：
# 小明和小红是一对龙凤胎。一天，他们的妈妈给了一张清单让他们去超市买东西。
# 买完东西出来后小明和小红发现这些东西非常多可能需要两个人都提一个袋子才能带走。
# 为了尽可能让双方提的袋子重量差不多，作为刚开始学习算法的小明和小红
# 决定思考一下如何分配两个袋子里的商品使得他们之间的重量差最小。

# 输入：
# 一行数据，n个数字，每个数字用空格隔开，代表商品的重量。
# 2 ≤ n ≤ 20
# 每个商品的重量都是整数，不超过 100000

# 输出：
# 两个袋子的最小重量差。

# 输入样例 1：
# 3 4 5 18 9 12 7

# 输出样例 1：
# 0

# 输入样例 2：
# 1 3 10 12 8

# 输出样例 2：
# 2

def bubble_sort(lists):
	n = len(lists) - 1
	for i in range(n):
		for j in range(n-i):
			if lists[j] > lists[j+1]:
				temp = lists[j]
				lists[j] = lists[j+1]
				lists[j+1] = temp

def find_weight(lists, target, differ):
	if not lists or lists[0] > target:
		differ.append(target)
	else:
		find_weight(lists[1:], target-lists[0], differ)
		find_weight(lists[1:], target, differ)

if __name__ == '__main__':
	nums = input().split(' ')
	weights = []
	weight_sum = 0
	differ = []

	for weight in nums:
		weights.append(int(weight))
		weight_sum += weights[-1]

	target = weight_sum//2
	bubble_sort(weights)

	find_weight(weights, target, differ)

	smaller_weight = target - min(differ)
	print(weight_sum - 2*smaller_weight)
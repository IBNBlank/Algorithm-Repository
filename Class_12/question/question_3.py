# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-06 19:58:57

# 描述
# 给定一个N个数的数组，请找出这里一共有多少个逆序对。

# 输入
# 一行数据，每个数字用空格隔开。最多60000个数字，每个数字大小在200000以内。

# 输出
# 逆序对数

# 输入样例：
# 5 3 8 4

# 输出样例：
# 3

def ways(battle_map, size, used_list, y, rest):
	result = 0

	if rest == 0:
		return 1
	elif size-y < rest:
		return 0
	else:
		result += ways(battle_map, size, used_list, y+1, rest)

		for j in range(size):
			if j not in used_list and  battle_map[y][j] == "#":
				used_list.append(j)
				result += ways(battle_map, size, used_list, y+1, rest-1)
				used_list.pop()

		return result

if __name__ == '__main__':
	size, num = input().split(" ")
	size = int(size)
	num = int(num)
	battle_map = []
	used_list = []

	for _ in range(size):
		battle_map.append(input())

	print(ways(battle_map, size, used_list, 0, num))

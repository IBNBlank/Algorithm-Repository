# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-22 19:54:04

# 描述：
# 勇士小明在经历九九八十一难后终于来到最后的魔城，准备找到大魔王决一死战。
# 但是大魔王其实有点怂，故意把魔城修得到处是障碍以阻挡勇士的前进。
# 魔城是一个n×n大小的迷宫，标记为0的地方可以走，标记为1的地方不能通过。
# 勇士小明从左上角开始每次走一步，只能向右或者向下走。
# 问勇士小明有多少种方法可以到达右下角的魔王的位置？

# 输入：
# 第一行是n
# 从第2行开始会有n行数据，每一行用0 1表示地图

# 输出：
# 小明有多少种方法可以到达右下角，没有的话输出0

# 输入样例 1：
# 3
# 0 0 0
# 0 1 0
# 0 0 0

# 输出样例 1：
# 2

# 输入样例 2：
# 3
# 0 0 0
# 0 0 0
# 0 0 0

# 输出样例 2：
# 16

matrix = []

def get_ways(x, y):
	global matrix
	answer = 0
	if matrix[x][y] == "1":
		return 0
	if x == 0 and y == 0:
		return 1
	else:
		if x > 0:
			answer += get_ways(x-1, y)
		if y > 0:
			answer += get_ways(x, y-1)
		return answer

if __name__ == '__main__':
	n = int(input())
	matrix = []
	for i in range(n):
		matrix.append(input().split(' '))

	print(get_ways(n-1, n-1))
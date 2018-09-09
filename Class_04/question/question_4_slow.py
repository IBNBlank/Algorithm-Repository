# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-26 19:26:49
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 07:25:49

class GameMessage(object):
	def __init__(self, n):
		self.x = 0
		self.y = 0
		self.target = (n-1, n-1)
		self.ways = 0

	def move(self, matrix):
		if matrix[self.x][self.y] == "1":
			return
		elif (self.x, self.y) == self.target:
			self.ways += 1
			return
		else:
			if self.x < self.target[0]:
				self.x += 1
				self.move(matrix)
				self.x -= 1

			if self.y < self.target[1]:
				self.y += 1
				self.move(matrix)
				self.y -= 1

	def get_ways(self):
		print(self.ways)

if __name__ == '__main__':
	n = int(input())
	matrix = []
	for i in range(n):
		matrix.append(input().split(' '))

	Game = GameMessage(n)
	Game.move(matrix)
	Game.get_ways()
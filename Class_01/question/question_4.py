# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-13 02:14:31
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-15 17:00:42

# 描述：
# 小明去商店买东西，他手里有一些零花钱，他希望能通过购买商店里的不同商品来正好花完他的零花钱（不然回家就要上交给老妈了）。
# 现在已知商店里各个商品的价格以及小明手里零花钱的总数，请问小明能够正好花完他的零花钱吗？

# 输入：
# 一共两行数据。
# 第一行为一组数字，用空格隔开，表示商店里不同商品的价格。
# 第二行为小明手里零花钱的总数。
# 注1：商品和小明零花钱的金额都是整数。
# 注2：商品数量不超过25个。

# 输出：
# 如果能够正好花完零花钱输出True，否则输出False。

# 输入样例 1：
# 1 2 3 4 5 6 7 8 9
# 12

# 输出样例 1：
# True

# 输入样例 2：
# 10 20 30 40
# 33

# 输出样例 2：
# False

##### QUESTION 4 #####
### 贪心 + 递归 ###
def bubble_sort(lists):
	n = len(lists) - 1
	for i in range(n):
		for j in range(n-i):
			if lists[j] > lists[j+1]:
				temp = lists[j]
				lists[j] = lists[j+1]
				lists[j+1] = temp

def buy(prices, money, count):
	if not prices or money <= 0:
		if money == 0 and count <= 25:
			return True
		else:
			return False
	else:
		price = prices.pop()
		if buy(prices, money-price, count+1):
			return True
		else:
			prices.append(price)
		price = prices.pop()
		if buy(prices, money, count):
			return True
		else:
			prices.append(price)

if __name__ == '__main__':
	nums = input().split(' ')
	prices = [int(price) for price in nums]
	bubble_sort(prices)
	money = int(input())

	if buy(prices, money, 0):
		print("True")
	else:
		print("False")

### 递归 ###
# def buy(prices, money, count):
# 	if not prices or money <= 0:
# 		if money == 0 and count <= 25:
# 			return True
# 		else:
# 			return False
# 	else:
# 		price = prices.pop()
# 		if buy(prices, money-price, count+1):
# 			return True
# 		else:
# 			prices.append(price)
# 		price = prices.pop()
# 		if buy(prices, money, count):
# 			return True
# 		else:
# 			prices.append(price)

# if __name__ == '__main__':
# 	nums = input().split(' ')
# 	prices = [int(price) for price in nums]
# 	money = int(input())

# 	if buy(prices, money, 0):
# 		print("True")
# 	else:
# 		print("False")

### 非递归 ###
# prices 很大时，效率很低 #
# def buy(prices, money):
# 	length = len(prices)
# 	count = 2 ** length
# 	price_sum = 0
# 	for i in range(count):
# 		for j in range(length):
# 			if i & (1<<j):
# 				price_sum += prices[j]
# 				if price_sum == money:
# 					return True
# 		price_sum = 0
# 	return False

# if __name__ == '__main__':
# 	nums = input().split(' ')
# 	prices = [int(price) for price in nums]
# 	money = int(input())

# 	if buy(prices, money):
# 		print("True")
# 	else:
# 		print("False")
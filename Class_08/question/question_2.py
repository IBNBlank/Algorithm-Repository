# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-09-09 07:29:16
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-10-14 16:26:18

# 描述
# 如果一个单词可以通过交换它单词里各个字母来得到另一个单词，那么我们称这两个单词为同一个变位词，比如eat和tea。
# 给定一组单词，请求出其中共有多少种变位词。
# 提示：可用Python自带的字典，不必自行设计哈希表。

# 输入
# 一行数据，每个单词用空格隔开，单词都是5个字母，最多有10000个单词。

# 输出
# 一个数字，有多少种变位词。
# 注：至少有两个不同的单词才算是变位词，只有一个单词的不算。

# 输入样例 1：
# abcde abdec acdbe eggii eiigg

# 输出样例 1：
# 2

# 输入样例 2：
# abcde cdefg efghi

# 输出样例 2：
# 0

def word_sort(s):
	word = list(s)
	word.sort()
	word = "".join(word)
	return word

def add_english_int(words_dict, word):
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict.update({word:1})

def words_num(words_dict):
	num = 0
	for val in words_dict.values():
		if val > 1:
			num += 1
	return num

if __name__ == '__main__':
	words_list = input().split(" ")
	words_dict = {}
	for word in words_list:
		add_english_int(words_dict, word_sort(word))
	print(words_num(words_dict))
# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 18:46:11
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-08-13 21:47:52

##### 列表list、 集合set、 元组tuple、 字典dictionary #####
#
# list VS tuple
# 1)区别：
# 	列表可以删减元素，元组生成后不可更改
# 2)元组使用场景：
# 	不希望被改变的数据
# 	哈希索引
#
# dictionary VS set
# 1)区别：
# 	字典 有 key，集合没有
# 	集合中的元素不会重复(添加已有元素不会重复)
#
##### 统计文章词频 #####

### 提升效率的关键：尽可能减少循环 ###

def word_count(words_list):
	words_set = set(words_list)
	words_dict = {}

	for word in words_list:
		if word:
			if word in words_list:
				words_dict[word] += 1
			else:
				words_dict[word] = 1

	print(words_dict)

if __name__ == '__main__':
	with open('i_have_adream.txt', 'r') as f:
		lines = f.readlines()
		s = ''

		for line in lines:
			line = line.replace(',', '')
			line = line.replace('.', '')
			line = line.replace(':', '')
			line = line.replace(';', '')
			line = line.replace('"', '')
			line = line.replace('!', '')
			line = line.replace('\n', '')
			s += line

		words_list = s.split(' ')
		word_count(words_list)
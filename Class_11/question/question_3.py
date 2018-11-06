# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-08-12 21:01:25
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:47:44

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

####################################
# def inverse_pairs(nums):
# 	count = 0
# 	sort_nums = [ i for i in nums ]
# 	sort_nums.sort()
# 	for num in sort_nums:
# 		count += nums.index(num)
# 		nums.remove(num)
# 	return count

# if __name__ == '__main__':
# 	strs = input().split(" ")
# 	nums = [ int(num) for num in strs ]
# 	print(inverse_pairs(nums))

###################################
def mergesort(nums):
	if len(nums) <= 1:
		return nums
	mid = int(len(nums)/2)
	left = mergesort(nums[:mid])
	right = mergesort(nums[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			global count
			count += len(left) - i
	result += left[i:]
	result += right[j:]
	return result

if __name__ == '__main__':
	count = 0
	strs = input().split(" ")
	nums = [ int(num) for num in strs ]
	mergesort(nums)
	print(count)

####################################
# def inversenum(a):
#     num = 0
#     length = len(a)
#     for i in range(length-1):
#         for j in range(i+1, length):
#             if a[i] > a[j]:
#                 num += 1
#     return num

# if __name__ == '__main__':
# 	strs = input().split(" ")
# 	nums = [ int(num) for num in strs ]
# 	print(inversenum(nums))
# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-25 14:22:44
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-11-04 18:49:41

class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

def qsort(start_index, end_index):
	if start_index >= end_index:
		return
	global intervals
	store_index = start_index + 1
	for i in range(start_index + 1, end_index):
		if intervals[i].start < intervals[start_index].start:
			intervals[i], intervals[store_index] = intervals[store_index], intervals[i]
			store_index += 1
	intervals[start_index], intervals[store_index - 1] = intervals[store_index - 1], intervals[start_index]
	qsort(start_index, store_index - 1)
	qsort(store_index, end_index)

s = input()
s_list = s.split(' ')
intervals = []
for i in s_list:
	start, end = i.split(':')
	intervals.append(Interval(int(start), int(end)))

qsort(0, len(intervals))

results = [intervals[0]]
for interval in intervals[1:]:
	if interval.start > results[-1].end:
		results.append(interval)
	else:
		start = min(interval.start, results[-1].start)
		end = max(interval.end, results[-1].end)
		results[-1] = Interval(start, end)

for interval in results:
	print('{}:{}'.format(interval.start, interval.end))
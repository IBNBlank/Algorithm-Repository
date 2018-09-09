# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-09-09 07:26:59
def solve(index, current_a_weight):
    global min_diff
    if index==0:
        #如果取第0号物品放到A包
        pack_a = current_a_weight +  items[0]
        pack_b = total_weight - pack_a
        diff = abs(pack_a - pack_b)
        if diff < min_diff:
            min_diff = diff

        #如果不取第0号物品放到A包
        pack_a = current_a_weight
        pack_b = total_weight - pack_a
        diff = abs(pack_a - pack_b)
        if diff < min_diff:
            min_diff = diff
    else:
        #如果取第index号物品放到A包
        solve(index - 1, current_a_weight + items[index])

        #如果不取第index号物品放到A包
        solve(index - 1, current_a_weight)


s = input()
s_list = s.split(' ')
items = [int(i) for i in s_list]
total_weight = sum(items)
min_diff = total_weight
solve(len(items) - 1, 0)
print(min_diff)
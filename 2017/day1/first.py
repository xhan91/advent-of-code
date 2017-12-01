#!/usr/bin/python

import sys

input = sys.argv[1]
input_arr = list(input)
input_arr.append(input_arr[0])
sum_num = 0
pre = None

for num in input_arr:
    num = int(num)
    if pre is None:
        pre = num
        continue
    else:
        sum_num += num if num == pre else 0
        pre = num

print sum_num
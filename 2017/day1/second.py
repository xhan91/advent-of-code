#!/usr/bin/python

import sys

input = sys.argv[1]
arr1 = list(input)
arr2 = list(input)
input_arr = arr1 + arr2
sum_num = 0
length = len(arr1)
steps = length / 2

for index, num in enumerate(input_arr):
    num = int(num)
    if index == length:
        break
    else:
        sum_num += num if num == int(input_arr[index + steps]) else 0

print sum_num
#!/usr/bin/python

def check_line(line):
    arr = list(map(int, line.split('\t')))
    return max(arr) - min(arr)

sum = 0
with open('input', 'r') as in_file:
    for line in in_file:
        line = line.strip()
        sum += check_line(line)

print sum

    
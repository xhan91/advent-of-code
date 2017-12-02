#!/usr/bin/python

def check_line(line):
    arr = list(map(int, line.split('\t')))
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            a = arr[i]
            b = arr[j]
            if b > a:
                a, b = b, a 
            if a % b == 0:
                print '{}/{}'.format(a, b)
                return a / b
            

sum = 0
with open('input', 'r') as in_file:
    for line in in_file:
        line = line.strip()
        sum += check_line(line)

print sum

    
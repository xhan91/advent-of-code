def is_valid(input):
    arr = input.split(' ')
    dic = {}
    for i in arr:
        if i in dic.keys():
            return 0
        dic[i] = 1
    return 1

with open('input', 'r') as in_file:
    sum = 0
    for line in in_file:
        sum += is_valid(line.strip())
    print sum
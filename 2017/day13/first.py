book = {}

with open('input', 'r') as input:
    for line in input:
        arr = line.strip().split(':')
        key = int(arr[0])
        value = int(arr[1])
        book[key] = value

sum = 0
for k,v in book.iteritems():
    if k % ((v - 1) * 2) == 0:
        sum += k * v

print sum
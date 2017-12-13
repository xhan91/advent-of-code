book = {}

with open('input', 'r') as input:
    for line in input:
        arr = line.strip().split(':')
        key = int(arr[0])
        value = int(arr[1])
        book[key] = value

i = 0
while True:
    sum = 0    
    for k,v in book.iteritems():
        if (k + i) % ((v - 1) * 2) == 0:
            sum += k * v
    if sum == 0 and i % ((book[0] - 1) * 2) != 0:
        break
    i += 1

print i


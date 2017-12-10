LENGTH_OF_ARRAY = 256

def process(arr, length, current):
    tmp_arr = []
    for i in range(length):
        pos = (i + current) % LENGTH_OF_ARRAY
        tmp_arr.append(arr[pos])
    tmp_arr.reverse()
    for i in range(length):
        pos = (i + current) % LENGTH_OF_ARRAY
        arr[pos] = tmp_arr[i]

with open('input', 'r') as input:
    for line in input:
        inputs = map(int, line.strip().split(','))

arr = list(range(LENGTH_OF_ARRAY))

current = 0
skip = 0
for length in inputs:
    process(arr, length, current)
    current += (length + skip)
    current %= LENGTH_OF_ARRAY
    skip += 1

print arr[0] * arr[1]
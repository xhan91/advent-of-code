

def get_max_index_value(arr):
    max_v = max(arr)
    index = arr.index(max_v)
    return index, max_v


def spread(arr):
    length = len(arr)
    index, max_v = get_max_index_value(arr)
    arr[index] = 0
    for i in range(max_v):
        index += 1
        index = index % length
        arr[index] += 1


with open('input', 'r') as input:
    for line in input:
        arr = map(int, line.strip().split('\t'))

# arr = [0,2,7,0]

key = ','.join(map(str, arr))
book = {}
sum_v = 0

while key not in book.keys():
    book[key] = 1
    sum_v += 1
    spread(arr)
    key = ','.join(map(str, arr))

print sum_v

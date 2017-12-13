book = {}

with open('input', 'r') as input:
    for line in input:
        arr = line.strip().split(' <-> ')
        key = arr[0]
        value = set(arr[1].split(', '))
        if key in book.keys():
            value |= book[key]
        for i in value:
            if value in book.keys():
                value |= book[i]
        book[key] = value
        for i in value:
            if i in book.keys():
                book[i] |= value
            else:
                book[i] = value

group = 0
key = book.keys()[0]
while key:
    value = book[key]
    for i in value:
        book.pop(i)
    group += 1
    if len(book.keys()) == 0:
        break
    key = book.keys()[0]

print group
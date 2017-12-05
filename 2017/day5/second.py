arr = []
with open('input', 'r') as input:
    for line in input:
        arr.append(int(line.strip()))

steps = 0
pos = 0
length = len(arr)

while pos < length and pos >= 0:
    old_pos = pos
    pos += arr[pos]
    if arr[old_pos] > 2:
        arr[old_pos] -= 1
    else:
        arr[old_pos] += 1
    steps += 1

print steps

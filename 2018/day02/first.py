input_array = []

with open('input.txt', 'r') as input:
  for line in input:
    input_array.append(line)

# return (0/1, 0/1)
def has2or3(s):
  m = {}
  for c in s:
    if c in m.keys():
      m[c] += 1
    else:
      m[c] = 1
  counts = m.values()
  has2 = 1 if 2 in counts else 0
  has3 = 1 if 3 in counts else 0
  return (has2, has3)

count2 = 0
count3 = 0
for input in input_array:
  result = has2or3(input)
  count2 += result[0]
  count3 += result[1]

print(count2 * count3)
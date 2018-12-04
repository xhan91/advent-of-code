input_array = []

with open('input.txt', 'r') as input:
  for line in input:
    input_array.append(line.strip())

def campare(s1, s2):
  count = 0
  l = len(s1)
  for i in range(l):
    if s1[i] != s2[i]:
      count += 1
  if count == 1:
    print(s1)
    print(s2)

for s1 in input_array:
  for s2 in input_array:
    campare(s1, s2)
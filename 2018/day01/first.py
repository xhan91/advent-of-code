result = 0

with open('input.txt', 'r') as input:
  for line in input:
    result += int(line)

print(result)
def is_fully(line):
  a, b = line.split(',')
  a1, a2 = a.split('-')
  b1, b2 = b.split('-')
  a1 = int(a1)
  a2 = int(a2)
  b1 = int(b1)
  b2 = int(b2)
  # Q1
  # if a1 >= b1 and a2 <= b2:
  #   return 1
  # if a1 <= b1 and a2 >= b2:
  #   return 1
  # return 0

  # Q2
  if a1 > b2 or a2 < b1:
    return 0
  return 1

result = 0
with open('input', 'r') as infile:
  for line in infile:
    result += is_fully(line.strip())
print(result)

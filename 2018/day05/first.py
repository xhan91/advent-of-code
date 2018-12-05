with open('input.txt', 'r') as input:
  line = input.read().strip()

def match(s1, s2):
  return s1.upper() == s2.upper() and s1 != s2

guard = True
while guard:
  guard = False
  length = len(line)
  i = 0
  keep = []
  while i < length - 1:
    if match(line[i], line[i + 1]):
      i += 2
      guard = True
    else:
      keep.append(i)
      i += 1
  if i == length - 1:
    keep.append(i)
  new_line = ''
  for i in keep:
    new_line += line[i]
  line = new_line

print(len(line))
input_array = []
r_map = {}

with open('input.txt', 'r') as input:
  for line in input:
    input_array.append(line.strip())

def calculate(s, r_map):
  tmp = s.split('@')[1].strip()
  tmp = tmp.split(': ')
  x, y = map(int, tmp[0].split(','))
  w, h = map(int, tmp[1].split('x'))
  for ww in range(w):
    for hh in range(h):
      pos = (x + ww + 1, y + hh + 1)
      if pos in r_map.keys():
        r_map[pos] += 1
      else:
        r_map[pos] = 1

for input in input_array:
  calculate(input, r_map)

count = 0
for c in r_map.values():
  if c > 1:
    count += 1

print(count)
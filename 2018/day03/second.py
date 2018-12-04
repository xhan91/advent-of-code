input_array = []
k_map = {}
key_map = {} # recoding all keys

with open('input.txt', 'r') as input:
  for line in input:
    input_array.append(line.strip())

def calculate(s, k_map, key_map):
  tmp = s.split('@')
  k = tmp[0].strip()[1:]
  key_map[k] = True
  tmp = tmp[1].strip().split(': ')
  x, y = map(int, tmp[0].split(','))
  w, h = map(int, tmp[1].split('x'))
  for ww in range(w):
    for hh in range(h):
      pos = (x + ww + 1, y + hh + 1)
      if pos in k_map.keys():
        k_map[pos].append(k)
      else:
        k_map[pos] = [k]

for input in input_array:
  calculate(input, k_map, key_map)

# when there's collision mark all keys as false
for k_array in k_map.values():
  if len(k_array) > 1:
    for k in k_array:
      key_map[k] = False

for k,v in key_map.items():
  if v:
    print(k)

state = [
  ['D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q'],
  ['F', 'H', 'Q', 'W', 'R', 'B', 'V'],
  ['H', 'S', 'V', 'C'],
  ['G', 'F', 'H'],
  ['Z', 'B', 'J', 'G', 'P'],
  ['L', 'F', 'W', 'H', 'J', 'T', 'Q'],
  ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'],
  ['F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D'],
  ['H', 'B', 'M', 'V', 'P', 'W']
]

# TEST
# state = [
#   ['N', 'Z'],
#   ['D', 'C', 'M'],
#   ['P']
# ]

def get_command(str):
  arr = str.split(' ')
  return int(arr[1]), int(arr[3]) - 1, int(arr[5]) - 1

def move(num, fro, to):
  state[to] = state[fro][:num] + state[to]
  state[fro] = state[fro][num:]

with open('input', 'r') as infile:
  for line in infile:
    num, fro, to = get_command(line)
    move(num, fro, to)

result = ''
for arr in state:
  result += arr[0]
print(result)
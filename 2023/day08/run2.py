file = "/Users/xhan91/workspace/python/advent-of-code/2023/day08/test2.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day08/input.txt"

class Node:
  def __init__(self, node, left, right):
    self.node = node
    self.left = left
    self.right = right

  def __repr__(self):
    return f"{self.node} ({self.left} {self.right})"

nodes = {}
instructions = None
with open(file, "r") as f:
  for line in f:
    line = line.strip()
    if not instructions:
      instructions = line
    elif line:
      node, rest = line.strip().split(" = ")
      left, right = rest[1:-1].split(", ")
      nodes[node] = Node(node, left, right)

result = 0
i = 0
current = []
for node in nodes.keys():
  if node[-1] == 'A':
    current.append(node)
while True:
  move = instructions[i]
  should_move = False
  temp = []
  for node in current:
    next_node = nodes[node].left if move == 'L' else nodes[node].right
    if next_node[-1] != 'Z':
      should_move = True
    temp.append(next_node)
  current = temp
  print(current)
  result += 1
  if not should_move:
    break
  i += 1
  if i == len(instructions):
    i = 0

print(result)
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day08/test1.txt"
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
current = nodes['AAA']
while True:
  move = instructions[i]
  current = nodes[current.left if move == 'L' else current.right]
  result += 1
  if current.node == 'ZZZ':
    break
  i += 1
  if i == len(instructions):
    i = 0

print(result)
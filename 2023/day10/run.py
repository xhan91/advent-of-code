file = "/Users/xhan91/workspace/python/advent-of-code/2023/day10/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day10/input.txt"

m = []
with open(file, "r") as f:
  count = 0
  for line in f:
    if 'S' in line:
      y = count
      x = line.index('S')
    line = list(line.strip())
    m.append(line)
    count += 1

mm = len(m[0])
mn = len(m)

count = 0
visited = set((y,x))

def bfs():
  global count
  global visited
  DIRES = {
    '-': [(0, 1), (0, -1)],
    '|': [(1, 0), (-1, 0)],
    'L': [(-1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    'F': [(1, 0), (0, 1)],
    'S': []
  }
  init = {
    (0,1): ['-', '7', 'J'],
    (0,-1): ['-', 'F', 'L'],
    (1,0): ['|', 'L', 'J'],
    (-1,0): ['|', 'F', '7'],
  }
  q = []
  for key, value in init.items():
    if m[y+key[0]][x+key[1]] in value:
      q.append((y+key[0], x+key[1]))
      print(m[y+key[0]][x+key[1]])
  
  while len(q) > 0:
    temp = []
    while len(q) > 0:
      i, j = q.pop(0)
      for a, b in DIRES[m[i][j]]:
        aa, bb = i+a, j+b
        if aa >= 0 and aa < mn and bb >= 0 and bb < mm and (aa,bb) not in visited:
          visited.add((aa, bb))
          temp.append((aa, bb))
    count += 1
    q = temp
  print(count)

bfs()
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

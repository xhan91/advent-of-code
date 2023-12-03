input = []
with open("/Users/xhan91/workspace/python/advent-of-code/2023/day03/input.txt", "r") as f:
  for line in f:
    input.append(list(line.strip()))

def calculate_gear(i,j,m,n):
  tiles = [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1, j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
  visited = set()
  buffer = ''
  num_found = []
  for a,b in tiles:
    if a >= 0 and a < m and b >= 0 and b < n:
      if input[a][b].isnumeric() and (a,b) not in visited:
        visited.add((a,b))
        buffer = input[a][b]
        c,d = b - 1, b + 1
        while c >= 0 and input[a][c].isnumeric():
          buffer = input[a][c] + buffer
          visited.add((a,c))
          c -= 1
        while d < n and input[a][d].isnumeric():
          buffer += input[a][d]
          visited.add((a,d))
          d += 1
        num_found.append(int(buffer))
        buffer = ''
  if len(num_found) == 2:
    return num_found[0] * num_found[1]
  return 0

m,n = len(input), len(input[0])
result = 0
buffer = ''
bufferConnect = False
for i in range(m):
  for j in range(n):
    if input[i][j] == '*':
      result += calculate_gear(i,j,m,n)

print(result)
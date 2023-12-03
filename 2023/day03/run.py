input = []
with open("/Users/xhan91/workspace/python/advent-of-code/2023/day03/input.txt", "r") as f:
  for line in f:
    input.append(list(line.strip()))

def if_connected(i,j,m,n):
  tiles = [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1, j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
  for a,b in tiles:
    if a >= 0 and a < m and b >= 0 and b < n:
      if not input[a][b].isnumeric() and input[a][b] != ".":
        return True
  return False

m,n = len(input), len(input[0])
result = 0
buffer = ''
bufferConnect = False
for i in range(m):
  for j in range(n):
    if input[i][j].isnumeric():
      bufferConnect = bufferConnect or if_connected(i,j,m,n)
      buffer += input[i][j]
    if not input[i][j].isnumeric() or j == n-1:
      if bufferConnect:
        result += int(buffer)
      buffer = ''
      bufferConnect = False

print(result)
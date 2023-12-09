file = "/Users/xhan91/workspace/python/advent-of-code/2023/day09/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day09/input.txt"

arrs = []
with open(file, "r") as f:
  for line in f:
    line = line.strip()
    arr = list(map(int, line.split(" ")))
    arrs.append(arr)

def find_last(arr):
  # find diff between every 2 numbers and save to a new array
  cur = arr
  arrs = [arr]
  temp = []
  while len(set(cur)) > 1 or sum(cur) != 0:
    for i in range(len(cur)-1):
      temp.append(cur[i+1] - cur[i])
    arrs.append(temp)
    cur = temp
    temp = []
  arrs.reverse()
  for i in range(1, len(arrs)):
    arrs[i].append(arrs[i][-1] + arrs[i-1][-1])
  return arrs[-1][-1]

result = 0
for arr in arrs:
  last = find_last(arr)
  result += last
print(result)

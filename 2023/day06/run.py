input = []
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day04/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day04/input.txt"

def tranform(arr):
  arr = map(lambda x : x.strip(), arr)
  arr = filter(lambda x : x != "", arr)
  return arr

def points(line):
  point = 1
  left, right = line.split(" | ")
  winning_numbers = tranform(left.split(": ")[1].split(" "))
  winning_numbers = set(winning_numbers)
  my_numbers = tranform(right.split(" "))
  for num in my_numbers:
    if num in winning_numbers:
      point *= 2
  return int(point / 2)

result = 0
with open(file, "r") as f:
  for line in f:
    result += points(line.strip())

print(result)
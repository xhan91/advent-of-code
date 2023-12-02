ANSWER = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

def test_line(line):
  game, records = line.split(": ")
  id = game.split(" ")[1]
  for record in records.split("; "):
    cubes = record.split(", ")
    for cube in cubes:
      num, color = cube.split(" ")
      if int(num) > ANSWER[color]:
        return (False, id)
  return (True, id)

result = 0
with open("/Users/xhan91/workspace/python/advent-of-code/2023/day02/input.txt", "r") as f:
  for line in f:
    is_valid, id = test_line(line.strip())
    if is_valid:
      result += int(id)

print(result)
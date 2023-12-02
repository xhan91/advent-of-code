def test_line(line):
  max_cubes = {
    "red": 0,
    "green": 0,
    "blue": 0,
  }
  game, records = line.split(": ")
  id = game.split(" ")[1]
  for record in records.split("; "):
    cubes = record.split(", ")
    for cube in cubes:
      num, color = cube.split(" ")
      if int(num) > max_cubes[color]:
        max_cubes[color] = int(num)
  return max_cubes["red"]* max_cubes["green"] * max_cubes["blue"]

result = 0
with open("/Users/xhan91/workspace/python/advent-of-code/2023/day02/input.txt", "r") as f:
  for line in f:
    power = test_line(line.strip())
    result += power

print(result)
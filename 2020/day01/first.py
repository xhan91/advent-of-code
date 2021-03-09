s = set()

with open("2020/day01/input.txt", "r") as infile:
  for line in infile:
    number = int(line.strip())
    s.add(number)

is_1000 = True

for number in s:
  if number != 1000:
    rest = 2020 - number
    if rest in s:
      print(number)
      print(rest)
      print(number * rest)
      is_1000 = False
      break

if is_1000:
  print(1000*1000)
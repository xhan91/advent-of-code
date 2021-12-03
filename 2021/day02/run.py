x = 0
y = 0

with open ("input.txt") as infile:
  for line in infile:
    input = line.split(' ')
    command = input[0]
    change = int(input[1])
    if command == 'forward':
      x += change
    if command == 'up':
      y -= change
    if command == 'down':
      y += change

print(x*y)

# Q2

x = 0
y = 0
aim = 0

with open ("input.txt") as infile:
  for line in infile:
    input = line.split(' ')
    command = input[0]
    change = int(input[1])
    if command == 'forward':
      x += change
      y += aim * change
    if command == 'up':
      aim -= change
    if command == 'down':
      aim += change

print(x*y)
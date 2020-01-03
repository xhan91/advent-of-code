def get_fuel(mass):
  sum = 0
  while mass > 6:
    mass = mass / 3 - 2
    sum += mass
  return sum

result = 0

with open('input.txt', 'r') as input:
  for line in input:
    result += get_fuel(int(line))

print(result)
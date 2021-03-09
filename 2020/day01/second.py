l = []

with open("2020/day01/input.txt", "r") as infile:
  for line in infile:
    number = int(line.strip())
    l.append(number)

l.sort()

def find_result(l):
  for i in range(len(l)):
    j = i + 1
    k = len(l) - 1
    rest = 2020 - l[i]
    while j < k:
      if l[j] + l[k] < rest:
        j = j + 1
      if l[j] + l[k] > rest:
        k = k - 1
      if l[j] + l[k] == rest:
        print(l[i], l[j], l[k])
        print(l[i] * l[j] * l[k])
        return

find_result(l)
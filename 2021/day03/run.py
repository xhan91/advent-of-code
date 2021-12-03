inputs = []

with open ("input.txt") as infile:
  for line in infile:
    inputs.append(line.strip())

# Q1
# length = len(inputs[0])

# digits0 = [0] * length
# digits1 = [0] * length

# for input in inputs:
#   for i in range(length):
#     if input[i] == '0':
#       digits0[i] += 1 
#     else:
#       digits1[i] += 1

# gamma = ''
# epsilon = ''
# for i in range(length):
#   if digits1[i] > digits0[i]:
#     gamma += '1'
#     epsilon += '0'
#   else:
#     gamma += '0'
#     epsilon += '1'

# print(gamma, epsilon)
# print(int(gamma, 2), int(epsilon, 2))
# print(int(gamma, 2) * int(epsilon, 2))

# Q2
pre = ''
i = 0
d0 = 0
d1 = 0

ox = inputs.copy()
co = inputs.copy()
while len(ox) > 1:
  for o in ox:
    if o[i] == '0':
      d0 += 1
    else:
      d1 += 1
  if d0 > d1:
    pre += '0'
  else:
    pre += '1'
  d0 = 0
  d1 = 0
  ox = list(filter(lambda a: a.startswith(pre) , ox))
  i += 1

print(ox[0])

pre = ''
i = 0
d0 = 0
d1 = 0

while len(co) > 1:
  for o in co:
    if o[i] == '0':
      d0 += 1
    else:
      d1 += 1
  if d0 <= d1:
    pre += '0'
  else:
    pre += '1'
  d0 = 0
  d1 = 0
  co = list(filter(lambda a: a.startswith(pre) , co))
  i += 1

print(co[0])
print(int(co[0], 2), int(ox[0], 2))
print(int(co[0], 2) * int(ox[0], 2))
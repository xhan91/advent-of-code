def is_valid(input):
  input_list = [int(x) for x in str(input)]
  count_list = [0] * 10
  x = 0
  for y in input_list:
    if x > y:
      return False
    count_list[y] += 1
    x = y

  return (2 in count_list)

# print(is_valid(112233))
# print(is_valid(123444))
# print(is_valid(111222))
# print(is_valid(111122))

count = 0
for i in range(256310, 732736+1):
  if is_valid(i):
    count += 1

print(count)

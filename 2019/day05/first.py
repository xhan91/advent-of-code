def is_valid(input):
  input_list = [int(x) for x in str(input)]
  valid = False
  for i in range(5):
    if input_list[i] == input_list[i+1]:
      valid = True
    if input_list[i] > input_list[i+1]:
      return False
  return valid

# print(is_valid(111111))
# print(is_valid(223450))
# print(is_valid(123789))

count = 0
for i in range(256310, 732736+1):
  if is_valid(i):
    count += 1

print(count)

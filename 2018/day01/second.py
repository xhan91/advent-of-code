result = 0
result_map = {0: 1}
input_array = []

with open('input.txt', 'r') as input:
  for line in input:
    input_array.append(int(line))

guard = True
while guard:
  for ii in input_array:
    result += ii
    try:
      if result_map[result]:
        print(result)
        guard = False
        break
    except:
      result_map[result] = 1
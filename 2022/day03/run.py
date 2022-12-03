def get_score(letter):
  score = ord(letter) - 96
  if score <= 0:
    score += 58
  return score

def get_letter(arr):
  a = arr[0]
  b = arr[1]
  c = arr[2]
  return list(set(a).intersection(set(b)).intersection(set(c)))[0]

result = 0
i = 0
input = []
with open('input', 'r') as infile:
  for line in infile:
    input.append(line.strip())
    i += 1
    if i == 3:
      letter = get_letter(input)
      result += get_score(letter)
      i = 0
      input = []

print(result)

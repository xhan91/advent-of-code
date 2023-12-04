input = []
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day04/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day04/input.txt"

def tranform(arr):
  arr = map(lambda x : x.strip(), arr)
  arr = filter(lambda x : x != "", arr)
  return arr

def points(line, id, multiplier):
  cards = 0
  left, right = line.split(" | ")
  winning_numbers = tranform(left.split(": ")[1].split(" "))
  winning_numbers = set(winning_numbers)
  my_numbers = tranform(right.split(" "))
  new_cards = {}
  for num in my_numbers:
    if num in winning_numbers:
      cards += 1
  for i in range(cards):
    new_cards[id + i + 1] = multiplier
  return new_cards

pile = {}
id = 0
with open(file, "r") as f:
  for line in f:
    id += 1
    if id not in pile:
      pile[id] = 1
    else:
      pile[id] += 1
    new_cards = points(line.strip(), id, pile[id])
    for k, v in new_cards.items():
      if k not in pile:
        pile[k] = v
      else:
        pile[k] += v
print(sum(pile.values()))
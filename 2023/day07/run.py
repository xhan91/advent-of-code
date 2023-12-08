from collections import Counter
import functools

file = "/Users/xhan91/workspace/python/advent-of-code/2023/day07/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day07/input.txt"

CARDS = {
  'A': 14,
  'K': 13,
  'Q': 12,
  'J': 11,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2
}

class Hand:
  def __init__(self, cards, bid):
    self.cards = cards
    self.counter = Counter(cards)
    self.bid = int(bid)

  def __repr__(self):
    return f"{self.cards} {self.bid}"

def compare(hand1, hand2):
  if len(hand1.counter) != len(hand2.counter):
    return len(hand2.counter) - len(hand1.counter)
  if max(hand1.counter.values()) != max(hand2.counter.values()):
    return max(hand1.counter.values()) - max(hand2.counter.values())
  for i in range(5):
    if CARDS[hand1.cards[i]] != CARDS[hand2.cards[i]]:
      return CARDS[hand1.cards[i]] - CARDS[hand2.cards[i]]

  

hands = []
with open(file, "r") as f:
  for line in f:
    line = line.strip()
    cards, bid = line.split(" ")
    hands.append(Hand(cards, bid))

hands = sorted(hands, key=functools.cmp_to_key(compare))
result = 0
for i, hand in enumerate(hands):
  result += hand.bid * (i + 1)
  print(hand, i+1)

print(result)
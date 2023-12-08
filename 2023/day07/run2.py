from collections import Counter
from copy import deepcopy
import functools

file = "/Users/xhan91/workspace/python/advent-of-code/2023/day07/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day07/input.txt"

CARDS = {
  'A': 14,
  'K': 13,
  'Q': 12,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2,
  'J': 1
}

class Hand:
  def __init__(self, cards, bid):
    self.cards = cards
    self.counter = Counter(cards)
    self.bid = int(bid)

  def __repr__(self):
    return f"{self.cards} {self.bid}"

def get_len(hand):
  l = len(hand.counter)
  if 'J' in hand.counter and l != 1: 
    l -= 1
  return l

def get_max(hand):
  m = max(hand.counter.values())
  if 'J' in hand.counter:
    if hand.counter['J'] == 5:
      return 5
    temp = deepcopy(hand.counter)
    del temp['J']
    m = max(temp.values()) + hand.counter['J']
  return m

def compare(hand1, hand2):
  l1 = get_len(hand1)
  l2 = get_len(hand2)
  if l1 != l2:
    return l2 - l1
  m1 = get_max(hand1)
  m2 = get_max(hand2)
  if m1 != m2:
    return m1 - m2
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
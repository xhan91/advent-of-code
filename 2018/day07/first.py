import string

char_req = {}
appered = {}
done = {}
result = ''

with open('input.txt', 'r') as input:
  for line in input:
    ent, pre = line[36], line[5]
    appered[ent] = True
    appered[pre] = True
    try:
      char_req[ent].append(pre)
    except:
      char_req[ent] = [pre]

appered = list(appered.keys())
appered.sort()

for c in appered:
  if c not in char_req.keys():
    done[c] = True
    result += c
  else:
    done[c] = False

guard = True
while guard:
  for c in appered:
    try:
      reqs = char_req[c]
      canMove = True
      for req in reqs:
        if not done[req]:
          canMove = False
      if canMove:
        result += c
        done[c] = True
        del char_req[c]
        break
    except:
      continue
  guard = False
  for check in done.values():
    if not check:
      guard = True
      break

print(result)
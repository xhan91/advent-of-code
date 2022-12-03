rule = {
  'A': {'X':4,'Y':8,'Z':3},
  'B': {'X':1,'Y':5,'Z':9},
  'C': {'X':7,'Y':2,'Z':6}
}

rule2 = {
  'A': {'X':0+3,'Y':3+1,'Z':6+2},
  'B': {'X':0+1,'Y':3+2,'Z':6+3},
  'C': {'X':0+2,'Y':3+3,'Z':6+1}
}

score = 0
with open('input', 'r') as infile:
  for line in infile:
    line = line.strip()
    i = line.split(' ')
    score += rule2[i[0]][i[1]]
print(score)
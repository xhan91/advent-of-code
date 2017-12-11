with open('input', 'r') as input:
    line = input.read().strip()

inputs = line.split(',')

verti = 0
hori = 0
fartest = 0

for i in inputs:
    if i == 'n':
        verti += 1
    if i == 'nw':
        verti += 0.5
        hori -= 0.5
    if i == 'ne':
        verti += 0.5
        hori += 0.5
    if i == 's':
        verti -= 1
    if i == 'sw':
        verti -= 0.5
        hori -= 0.5
    if i == 'se':
        verti -= 0.5
        hori += 0.5
    fartest = max(fartest, verti + hori)

# first
print verti + hori
# second
print fartest
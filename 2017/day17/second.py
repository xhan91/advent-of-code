STEPS = 370

pos = 0
for i in range(1, 50000000):
    pos = (pos + STEPS) % i + 1
    if pos == 1:
        res = i

print res
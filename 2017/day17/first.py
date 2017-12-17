STEPS = 370
buffer = [0]

pos = 0
for i in range(1, 2018):
    pos = (pos + STEPS) % len(buffer) + 1
    buffer.insert(pos, i)

print buffer[pos + 1]
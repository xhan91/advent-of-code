book = {}

with open('input', 'r') as input:
    l = 0
    for line in input:
        arr = list(line.strip())
        for i, v in enumerate(arr):
            book[(i,l)] = int(v)
        l += 1

def mark_linked(key):
    x, y = key
    # up
    if y > 0 and book[(x, y-1)] and (x, y-1) not in is_marked.keys():
        is_marked[(x, y-1)] = 1
        mark_linked((x, y-1))
    # down
    if y < 127 and book[(x, y+1)] and (x, y+1) not in is_marked.keys():
        is_marked[(x, y+1)] = 1
        mark_linked((x, y+1))
    # left
    if x > 0 and book[(x-1, y)] and (x-1, y) not in is_marked.keys():
        is_marked[(x-1, y)] = 1
        mark_linked((x-1, y))
    # right
    if x < 127 and book[(x+1, y)] and (x+1, y) not in is_marked.keys():
        is_marked[(x+1, y)] = 1
        mark_linked((x+1, y))



is_marked = {}
groups = 0

for i in range(128):
    for j in range(128):
        if book[(i,j)] and (i,j) not in is_marked.keys():
            groups += 1
            is_marked[(i,j)] = 1
            mark_linked((i,j))

print groups
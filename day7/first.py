
# double linked list like structure

class Node:
    def __init__(self, name, weight):
        self.up = []
        self.down = None
        self.name = name
        self.weight = weight        

    def add_up(self, name):
        self.up.append(name)

    def add_down(self, name):
        self.down = name


nodes = {}
links = {}

with open('input', 'r') as input:
    for line in input:
        l_arr = line.strip().split(' -> ')
        ll_arr = l_arr[0].split(' ')
        # parse node
        name = ll_arr[0]
        weight = int(ll_arr[1][1:-1])
        node = Node(name, weight)
        nodes[name] = node
        # parse link
        if len(l_arr) > 1:
            links[name] = l_arr[1]

# link nodes
for k, v in links.iteritems():
    for kk in v.split(', '):
        nodes[kk].add_down(nodes[k])
        nodes[k].add_up(nodes[kk])

# find root
for k, v in nodes.iteritems():
    if not v.down:
        print k
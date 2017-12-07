
# double linked list like structure
class Node:
    def __init__(self, name, weight):
        self.up = []
        self.down = None
        self.total = None
        self.name = name
        self.weight = weight        

    def add_up(self, node):
        self.up.append(node)

    def add_down(self, node):
        self.down = node

    def check_balance_and_get_weight(self):
        if len(self.up) > 0:
            sub_weights = map(lambda x: x.check_balance_and_get_weight(), self.up)
            mark = sub_weights[0]
            for i in sub_weights:
                if mark != i:
                    for node in self.up:
                        print node.name, node.total, node.weight
                    print "==="
            self.total = reduce(lambda a, b: a + b, sub_weights) + self.weight
        else:
            self.total = self.weight
        return self.total



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

# root is ahnofa
root = nodes['ahnofa']
root.check_balance_and_get_weight()

# Not very clean solution but let call it a day!
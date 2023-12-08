class Interval:
    def __init__(self, start, end, shift):
        self.start = start
        self.end = end
        self.shift = shift

    def __repr__(self):
        return f"[{self.start}, {self.end}, {self.shift}]"

class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max_end = interval.end
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):
        if not node:
            return IntervalNode(interval)

        if interval.start < node.interval.start:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        if node.max_end < interval.end:
            node.max_end = interval.end

        return node

    def point_search(self, point):
        result = self.overlap_search(Interval(point, point, 0))
        if result:
            return point + result.shift
        else:
            return point

    def overlap_search(self, interval):
        return self._overlap_search(self.root, interval)

    def _overlap_search(self, node, interval):
        if not node:
            return None

        if self._do_overlap(node.interval, interval):
            return node.interval

        if node.left and node.left.max_end >= interval.start:
            return self._overlap_search(node.left, interval)

        return self._overlap_search(node.right, interval)

    @staticmethod
    def _do_overlap(interval1, interval2):
        return interval1.start <= interval2.end and interval2.start <= interval1.end

file = "/Users/xhan91/workspace/python/advent-of-code/2023/day05/test1.txt"
file = "/Users/xhan91/workspace/python/advent-of-code/2023/day05/input.txt"

maps = []
current_map = IntervalTree()

with open(file, "r") as f:
  for line in f:
    line = line.strip()
    if line.startswith("seeds:"):
        seeds = line.split(":")[1].strip().split(" ")
        seeds = map(int, seeds)
    elif line.endswith("map:"):
        maps.append(current_map)
        current_map = IntervalTree()
    elif line:
        params = line.split(" ")
        params = map(int, params)
        des, src, ran = params
        current_map.insert(Interval(src, src + ran - 1, des - src))
  maps.append(current_map)

results = []
for seed in seeds:
    point = seed
    for m in maps:
        point = m.point_search(point)
    results.append(point)
print(results)
print(min(results))

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
        self.min_start = interval.start
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

        if node.min_start > interval.start:
            node.min_start = interval.start

        return node

    def overlap_search(self, interval):
        return self._overlap_search(self.root, interval)

    def _overlap_search(self, node, interval):
        if not interval:
            return []
        result = []
        if not node:
            result.append(interval)
            return result

        if self._do_overlap(node.interval, interval):
            # break input interval into 2 parts
            left = None
            right = None
            if interval.start < node.interval.start:
                left = Interval(interval.start, node.interval.start - 1, interval.shift)
            if interval.end > node.interval.end:
                right = Interval(node.interval.end + 1, interval.end, interval.shift)
            middle = Interval(max(node.interval.start, interval.start), min(node.interval.end, interval.end), interval.shift + node.interval.shift)
            result += self._overlap_search(node.left, left)
            result.append(middle)
            result += self._overlap_search(node.right, right)
            return result
        
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
        seeds = list(map(int, seeds))
    elif line.endswith("map:"):
        maps.append(current_map)
        current_map = IntervalTree()
    elif line:
        params = line.split(" ")
        params = map(int, params)
        des, src, ran = params
        current_map.insert(Interval(src, src + ran - 1, des - src))
  maps.append(current_map)

min_result = float('inf')
seed_intervals = []
for i in range(0, len(seeds), 2):
    seed_intervals.append(Interval(seeds[i], seeds[i] + seeds[i+1] - 1, 0))

for seed_interval in seed_intervals:
    start = [seed_interval]
    for m in maps:
        for result in start:
            start = m.overlap_search(result)
        start = list(map(lambda x: Interval(x.start + x.shift, x.end + x.shift, 0), start))
    for result in start:
        if result.start + result.shift < min_result:
            min_result = result.start + result.shift
    
print(min_result)

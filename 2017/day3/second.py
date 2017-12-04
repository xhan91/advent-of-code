class Day3:

    def __init__(self):
        self.grid = dict()
        self.grid[(0, 0)] = 1
        self.limit = 1
        self.side = 0
        self.x = 0
        self.y = 0
        self.move = {
            0: self.right,
            1: self.up,
            2: self.left,
            3: self.down
        }

    @staticmethod
    def calc(x, y, grid):
        surrounding = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]
        sum = 0
        for key in surrounding:
            if key in grid.keys():
                sum += grid[key]
        return sum

    def up(self):
        self.y += 1
        if abs(self.y) == self.limit:
            self.turn()

    def down(self):
        self.y -= 1
        if abs(self.y) == self.limit:
            self.turn()

    def left(self):
        self.x -= 1
        if abs(self.x) == self.limit:
            self.turn()

    def right(self):
        self.x += 1
        if abs(self.x) == self.limit:
            self.turn()

    def turn(self):
        self.side = (self.side + 1) % 4
        if self.side == 0:
            self.limit += 1

    def calc_input(self, input):
        result = 0
        while result < input:
            self.move[self.side]()
            result = Day3.calc(self.x, self.y, self.grid)
            self.grid[(self.x, self.y)] = result
        return result


input = 312051
day3 = Day3()
print(day3.calc_input(input))

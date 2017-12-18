import string

class Day18:
    def __init__(self):
        self.REGISTERS = { x: 0 for x in string.ascii_lowercase }
        self.book = {
            'set': self.c_set,
            'add': self.c_add,
            'mul': self.c_mul,
            'mod': self.c_mod,
            'snd': self.snd,
            'jgz': self.jgz,
        }
        self.sound = None
        self.index = 0

    def c_set(self, x, y):
        try:
            self.REGISTERS[x] = int(y)
        except:
            self.REGISTERS[x] = self.REGISTERS[y]

    def c_add(self, x, y):
        try:
            self.REGISTERS[x] += int(y)
        except:
            self.REGISTERS[x] += self.REGISTERS[y]

    def c_mul(self, x, y):
        try:
            self.REGISTERS[x] *= int(y)
        except:
            self.REGISTERS[x] *= self.REGISTERS[y]

    def c_mod(self, x, y):
        try:
            self.REGISTERS[x] %= int(y)
        except:
            self.REGISTERS[x] %= self.REGISTERS[y]

    def snd(self, x):
        try:
            self.sound = int(x)
        except:
            self.sound = self.REGISTERS[x]

    def jgz(self, x, y):
        try:
            if self.REGISTERS[x] > 0:
                self.index += int(y)
            else:
                self.index += 1
        except:
            if x > 0:
                self.index += int(y)
            else:
                self.index += 1

    def call(self, command):
        if command[0] == 'rcv':
            if self.REGISTERS[command[1]] != 0:
                print self.sound
                return True
        else:
            self.book[command[0]](*command[1:])
        if command[0] != 'jgz':
            self.index += 1
        return False


if __name__ == '__main__':
    commands = []
    with open('input', 'r') as input:
        for line in input:
            commands.append(line.strip().split(' '))

    day = Day18()
    i = 0
    while not day.call(commands[i]):
        i = day.index

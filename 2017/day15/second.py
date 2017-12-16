X = 2147483647

A = 699
B = 124

factor_a = 16807
factor_b = 48271

class Generator:
    def __init__(self, factor, first):
        self.factor = factor
        self.value = first
        self.check = None

    def get_value(self):
        return self.value

    def next_good(self):
        self.next()
        while not self.check(self.value):
            self.next()

    def next(self):
        self.value = (self.value * self.factor) % X


def is_multi_of_4(n):
    n = str(n)
    if len(n) > 2:
        n = int(n[-2:])
    else:
        n = int(n)
    return n % 4 == 0


def is_multi_of_8(n):
    n = str(n)
    if len(n) > 3:
        n = int(n[-3:])
    else:
        n = int(n)
    return n % 8 == 0


gen_a = Generator(factor_a, A)
gen_b = Generator(factor_b, B)
gen_a.check = is_multi_of_4
gen_b.check = is_multi_of_8

sum = 0

def is_same_16bit(a, b):
    # both a and b are int
    a = bin(a)[2:].zfill(16)[-16:]
    b = bin(b)[2:].zfill(16)[-16:]
    return a == b

for i in range(5000000):
    gen_a.next_good()
    a = gen_a.get_value()
    gen_b.next_good()
    b = gen_b.get_value()
    if is_same_16bit(a,b):
        sum += 1

print sum

    
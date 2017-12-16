X = 2147483647

A = 699
B = 124

factor_a = 16807
factor_b = 48271

class Generator:
    def __init__(self, factor, first):
        self.factor = factor
        self.value = first

    def get_value(self):
        return self.value

    def next(self):
        self.value = (self.value * self.factor) % X

gen_a = Generator(factor_a, A)
gen_b = Generator(factor_b, B)

sum = 0

def is_same_16bit(a, b):
    # both a and b are int
    a = bin(a)[2:].zfill(16)[-16:]
    b = bin(b)[2:].zfill(16)[-16:]
    return a == b

for i in range(40000000):
    gen_a.next()
    a = gen_a.get_value()
    gen_b.next()
    b = gen_b.get_value()
    if is_same_16bit(a,b):
        sum += 1

print sum

    
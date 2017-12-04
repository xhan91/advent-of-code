input = 312051

outter = 1

while (outter * outter < input):
    outter += 2

inner = outter - 2

side = (outter * outter - input) / (outter - 1)
# 0 - down, 1 - left, 2 - up, 3 - right

def c_down(input, outter, inner):
    vertical = outter / 2
    horizontal = input - (outter * outter - outter / 2)
    return vertical + abs(horizontal)

print c_down(input, outter, inner)
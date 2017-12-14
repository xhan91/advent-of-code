import binascii

input = 'jzgqcdpd'

LENGTH_OF_ARRAY = 256

def process(arr, length, current):
    tmp_arr = []
    for i in range(length):
        pos = (i + current) % LENGTH_OF_ARRAY
        tmp_arr.append(arr[pos])
    tmp_arr.reverse()
    for i in range(length):
        pos = (i + current) % LENGTH_OF_ARRAY
        arr[pos] = tmp_arr[i]

def knot_hash(input):
    inputs = map(ord, list(input))

    # print(inputs)
    inputs += [17, 31, 73, 47, 23]

    arr = list(range(LENGTH_OF_ARRAY))

    current = 0
    skip = 0
    for i in range(64):
        for length in inputs:
            process(arr, length, current)
            current += (length + skip)
            current %= LENGTH_OF_ARRAY
            skip += 1

    # arr is sparse hash
    dense_hash = []
    for i in range(16):
        tmp_arr = arr[i * 16 : (i + 1) * 16]
        tmp = reduce(lambda a, b: a ^ b, tmp_arr)
        dense_hash.append(tmp)

    res = ""
    for n in dense_hash:
        tmp = hex(n)[2:]
        if len(tmp) == 1:
            tmp = '0' + tmp
        res += tmp
        
    return res

def destruct_hash(hh):
    scale = 16
    num_of_bits = 128
    binary_string = bin(int(hh, scale))[2:].zfill(num_of_bits)
    return binary_string

sum = 0
output = open('input','w')

for i in range(128):
    ii = "{}-{}".format(input, i)
    bb = destruct_hash(knot_hash(ii))
    output.write(bb + '\n')
    bb = bb.replace("0", "")
    sum += len(bb)

output.close()
print sum
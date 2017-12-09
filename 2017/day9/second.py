
def evaluate(input):
    """
    input is a str, we loop it
    """
    sum = 0
    is_garbage = False
    length = len(input)
    i = 0
    while i < length:
        v = input[i]
        if is_garbage:
            if v == '!':
                i += 1
            elif v == '>':
                is_garbage = False
            else:
                sum += 1
        else:
            if v == '<':
                is_garbage = True
        i += 1
    return sum
        

with open('input', 'r') as input:
    for line in input:
        print evaluate(line.strip())
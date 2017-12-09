
def evaluate(input):
    """
    input is a str, we loop it
    """
    sum = 0
    current = 0
    is_garbage = False
    length = len(input)
    i = 0
    while i < length:
        v = input[i]
        if is_garbage:
            if v == '!':
                i += 1
            if v == '>':
                is_garbage = False
        else:
            if v == '{':
                current += 1
            if v == '}':
                sum += current
                current -= 1
            if v == '<':
                is_garbage = True
        i += 1
    return sum
        

with open('input', 'r') as input:
    for line in input:
        print evaluate(line.strip())
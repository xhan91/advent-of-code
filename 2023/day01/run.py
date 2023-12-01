#start from line 1, find the first number from left as number x, then find the first number from right as number y, then combine xy into a two digit nubmer
#then move on to each line below and repeat step 1 
#then add all the two digit numbers together and print the result

DIGITS = set(list("0123456789"))
DIGIT_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_two_digit_number(line):
    i = 0
    j = len(line) - 1
    x = -1
    y = -1
    while True:
        if line[i] in DIGITS:
            x = int(line[i])
        else:
            i += 1
        if line[j] in DIGITS:
            y = int(line[j])
        else:
            j -= 1
        if x != -1 and y != -1:
            return x * 10 + y

result = 0
with open("test.txt", "r") as f:
    for line in f:
        line = process_the_line(line)
        print(line)
        result += find_two_digit_number(line)

print(result)

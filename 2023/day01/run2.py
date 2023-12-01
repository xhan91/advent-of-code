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

def find_first_digit(line):
    for i in range(len(line)):
        if line[i] in DIGITS:
            return int(line[i])
        for key, value in DIGIT_MAP.items():
            if line[i:].startswith(key):
                return value
        
def find_second_digit(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i] in DIGITS:
            return int(line[i])
        for key, value in DIGIT_MAP.items():
            if line[:i].endswith(key):
                return value
result = 0
with open("input.txt", "r") as f:
    for line in f:
        result += find_first_digit(line) * 10 + find_second_digit(line)

print(result)

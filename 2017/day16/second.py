with open('input', 'r') as input:
    for line in input:
        moves = line.strip().split(',')

INIT_STR = 'abcdefghijklmnop'
BILLION = 1000000000
dancers = list(INIT_STR)

def spin(n, in_arr):
    n = int(n)
    return in_arr[-n:] + in_arr[:-n]

def exchange(n, in_arr):
    sub = n.split('/')
    a = int(sub[0])
    b = int(sub[1])
    in_arr[a], in_arr[b] = in_arr[b], in_arr[a]
    return in_arr

def partner(n, in_arr):
    a, b = (i for i in n.split('/'))
    i = in_arr.index(a)
    j = in_arr.index(b)
    in_arr[i], in_arr[j] = in_arr[j], in_arr[i]
    return in_arr    


book = {
    's': spin,
    'x': exchange,
    'p': partner,
}

dancing_book = {}
dancing_book[0] = INIT_STR
count = 0

dancers_str = ''
while True:
    for move in moves:
        m_type = move[0]
        move = move[1:]
        dancers = book[m_type](move, dancers)
    dancers_str = ''.join(dancers)
    if dancers_str == INIT_STR:
        break
    else:
        count += 1
        dancing_book[count] = dancers_str

res = BILLION % (count + 1)
print dancing_book[res]
print count
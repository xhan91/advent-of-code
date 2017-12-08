
regs = {}

conditions = []
actions = []

with open('input', 'r') as input:
    for line in input:
        arr = line.strip().split(' if ')
        # parse key
        sub_arr1 = arr[0].split(' ')
        key = sub_arr1[0]
        regs[key] = 0
        # parse action
        sub_arr1[0] = 'regs[\'' + sub_arr1[0] + '\']'
        sub_arr1[1] = '+=' if sub_arr1[1] == 'inc' else '-='
        sub_arr1[2] = '(' + sub_arr1[2] + ')'
        action = ' '.join(sub_arr1)
        actions.append(action)
        sub_arr2 = arr[1].split(' ')
        sub_arr2[0] = 'regs[\'' + sub_arr2[0] + '\']'
        condition = ' '.join(sub_arr2)
        conditions.append(condition)

is_triggered = True
length = len(conditions)

# print actions
# print conditions

max_v = 0

for i in range(length):
    if eval(conditions[i]):
        exec(actions[i])
    # for second
    max_v = max(max_v, max(regs.values()))

# for first
# max_v = max(regs.values())

print max_v
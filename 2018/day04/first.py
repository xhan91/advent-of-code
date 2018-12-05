date_guard = {}
date_timetable = {}
guard_time = {}

def processLine(s, date_guard, date_timetable):
  dateTime, action = s.split('] ')
  date, time = dateTime[6:].split(' ')
  minite = int(time.split(':')[1])
  if action[0] == 'G':
    guard = action.split(' ')[1][1:]
    date_guard[date] = guard
    if date not in date_timetable.keys():
      date_timetable[date] = [''] * 60
  elif action[0] == 'w':
    if date not in date_timetable.keys():
      date_timetable[date] = [''] * 60
    else:
      date_timetable[date][minite] = 'w'
  elif action[0] == 'f':
    if date not in date_timetable.keys():
      date_timetable[date] = [''] * 60
    else:
      date_timetable[date][minite] = 's'

with open('input.txt', 'r') as input:
  for line in input:
    processLine(line.strip(), date_guard, date_timetable)

for timetable in date_timetable.values():
  status = '.'
  for i in range(60):
    if timetable[i] == 'w':
      status = '.'
    if timetable[i] == 's':
      status = '#'
    timetable[i] = status

# for d in date_guard.keys():
#   print(d, date_guard[d], ''.join(date_timetable[d]))

for date, timetable in date_timetable.items():
  if date in date_guard.keys():
    guard = date_guard[date]
  else:
    continue
  if guard not in guard_time.keys():
    guard_time[guard] = 0
  for i in range(60):
    if timetable[i] == '#':
      guard_time[guard] += 1

the_time = max(guard_time.values())
for k,v in guard_time.items():
  if v == the_time:
    the_guard = k

print(the_guard)

for d in date_guard.keys():
  if date_guard[d] == '3571':
    print(d, date_guard[d], ''.join(date_timetable[d]))

all_timetable = [0] * 60
for date, guard in date_guard.items():
  if guard == the_guard:
    timetable = date_timetable[date]
    for i in range(60):
      if timetable[i] == '#':
        all_timetable[i] += 1

tmp = list(map(str, all_timetable))
print(''.join(tmp))

max_minute = max(all_timetable)
for i in range(60):
  if all_timetable[i] == max_minute:
    the_minute = i
    break

print(int(the_guard) * the_minute)
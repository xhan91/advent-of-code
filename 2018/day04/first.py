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
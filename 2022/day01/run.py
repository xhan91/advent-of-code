elf = []
current = 0
with open('input', 'r') as infile:
  for line in infile:
    if line.strip():
      current += int(line.strip())
    else:
      elf.append(current)
      current = 0
elf.sort(reverse=True)
print(sum(elf[:3]))
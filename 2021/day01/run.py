nums = []

with open ("input.txt") as infile:
  for line in infile:
    nums.append(int(line))

pre = nums[0]
count = 0
for num in nums:
  if num - pre > 0:
    count += 1
  pre = num

print(count)

# Q2
count = 0
for i in range(len(nums)):
  if i > 2 and nums[i] > nums[i-3]:
    count += 1
print(count)
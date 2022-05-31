n = int(input())
a = [int(x) for x in input().split(" ")]
list = [0] * 360
list[0] = 1
now = 0
for line in a:
  list[(now + line)%360] = 1
  now = now + line
count = 0
Max = 0
FB = True
FC = 0
for y in list:
  if y == 1:
    if FB:
      FB = False
      FC += count
    if Max < count:
      Max = count
    count = 0
  count += 1
count += FC
if Max < count:
  Max = count
print(Max)

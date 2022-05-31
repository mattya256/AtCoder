N = int(input())
A = list(map(int,input().split()))
count0 = 0
count1 = 0
min = 0
max = 0
for a in A:
  if a == 0:
    count0 -= 1
    count1 -= 1
  if a == 1:
    count0 += 1
    count1 += 1
  if count0 > 0:
    count0 = 0
  if count1 < 0:
    count1 = 0
  if min > count0:
    min = count0
  if max < count1:
    max = count1
print(max - min + 1)
  

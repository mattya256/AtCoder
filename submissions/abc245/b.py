N = int(input())
A = list(map(int,input().split()))
A.sort()
count = 0
for x in A:
  if x == count:
    count += 1
print(count)
  

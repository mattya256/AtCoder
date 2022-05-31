N = int(input())
A = []
for x in range(N):
  A.append(list(map(int,input().split())))
sum2 = 1
for x in A:
  sum = 0
  for a in x:
    sum += a
  sum2 *= sum
  sum2 = sum2 % (10**9 + 7)
print(sum2)
  

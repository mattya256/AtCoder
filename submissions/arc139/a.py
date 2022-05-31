N = int(input())
T = list(map(int,input().split()))

a = 0
for x in range(N):
  a += 1
  if a % 2** T[x] == 0 and (a // 2** T[x])%2 == 1:
    pass
  else:
    bb = a
    a = (a//(2** T[x]) + 1) * 2** T[x]
    if a % 2** T[x] == 0 and (a // 2** T[x])%2 == 1:
      pass
    else:
      a += 2** T[x]
print(a)

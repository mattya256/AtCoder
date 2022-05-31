N,K = map(int,input().split())
A = list(map(int,input().split()))

for i,a in enumerate(A):
  A[i] = [A[i],i]
  
A.sort()
#print(A)
MAX = -1
before = -1
beforeMAX = -1
MINcomp = 4 * 10 ** 5 + 4
for a in A:
  if a[1] < K:
    if before != a[0]:
    	beforeMAX = MAX
    MAX = max(a[1],MAX)
    before = a[0]
  else:
    if before == a[0]:
      if beforeMAX != -1:
        MINcomp = min(a[1]  - beforeMAX, MINcomp)
    elif MAX != -1:
      MINcomp = min(a[1]  - MAX, MINcomp)
  #print(a,MAX,MINcomp,before,beforeMAX)
if MINcomp == 4 * 10 ** 5 + 4:
  print(-1)
else:
  print(MINcomp)

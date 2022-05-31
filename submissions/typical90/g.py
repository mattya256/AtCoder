N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())
B = []
for x in range(Q):
  B.append(int(input()))
BB = B.copy()
B.sort()
AC = 0
BC = 0
dict = {}
while(True):
  AN = ANN = A[AC]
  BN = B[BC]
  if AC < len(A) - 1:
    ANN = A[AC+1]
  if BN > ANN and AC < len(A) - 1 :
    AC +=1
  #elif AN <= BN and BN <= ANN:
  else:
    dict[BN] = min(abs(AN-BN),abs(ANN-BN))
    BC += 1
  if BC == len(B):
    break

for bb in BB:
  print(dict[bb])

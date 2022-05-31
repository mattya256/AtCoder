N,X = map(int,input().split())

T0 = ((N + (N % 2))//2)
if N % 2 == 1:
  T1 = ((N + (N % 2))//2)
else:
  T1 = ((N)//2) + 1

PList = [True for _ in range(N+1)]
OL = []

if X == T0:
  Z = 1
  S = T1
elif X == T1:
  Z = 0
  S = T0
else:
  if X < T0:
    S = T1
    Z = 0
  else:
    S = T0
    Z = 1
L = S
R = S
count = 0
OL.append(X)
PList[X] = False
count += 1
while(True):
  #print(OL,PList,L,R,Z,X,T0,T1)
  if Z == 0:
    while(True):
      if PList[L]:
        PList[L] = False
        count += 1
        OL.append(L)
        Z = 1
        L -= 1
        break
      else:
        L -= 1
  else:
    while(True):
      if PList[R]:
        PList[R] = False
        count += 1
        OL.append(R)
        Z = 0
        R += 1
        break
      else:
        R += 1
  if count == N:
    break
print(*OL)

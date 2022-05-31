N = int(input())
AA = [0]
BB = [0]
AAsum = BBsum = 0
for i in range(N):
  xx = list(map(int,input().split()))
  if xx[0] == 1:
    AAsum += xx[1]
  else:
    BBsum += xx[1]
  AA.append(AAsum)
  BB.append(BBsum)
Q = int(input())
for i in range(Q):
  AS = 0
  BS = 0
  L,R = list(map(int,input().split()))
  AS += AA[R] - AA[L-1]
  BS += BB[R] - BB[L-1]
  print(str(AS) + " " + str(BS))

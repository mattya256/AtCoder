N = int(input())
MAXNUM = -1
MAXIND = -1
Dict = {}
for i in range(N):
  WW = input().split()
  S = WW[0]
  T = int(WW[1])
  if S in Dict:
    pass
  else:
    Dict[S] = True
    if T > MAXNUM:
      MAXNUM = T
      MAXIND = i+1
print(MAXIND)

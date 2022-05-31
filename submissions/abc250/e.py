N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())
Dict = {}
count = 0
for a in A:
  if a in Dict:
    pass
  else:
    Dict[a] = count
    count += 1
for b in B:
  if b in Dict:
    pass
  else:
    Dict[b] = count
    count += 1
AA = []
MAX = -1
for a in A:
  MAX = max(MAX,Dict[a])
  AA.append(MAX)
BB = []
MAX = -1
count = 0
DictB = {}
for b in B:
  if b in DictB:
    pass
  else:
    DictB[b] = 0
    count += 1
  MAX = max(MAX,Dict[b])
  BB.append([count,MAX])
for _ in range(Q):
  x,y = list(map(int,input().split()))
  x -= 1
  y -= 1
  if AA[x] == BB[y][1] and BB[y][1] + 1 == BB[y][0]:
    print("Yes")
  else:
    print("No")
  

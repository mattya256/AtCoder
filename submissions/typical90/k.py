H,W = map(int,input().split())
P = []
for h in range(H):
  l = list(map(int,input().split()))
  P.append(l)
HL = [[]]
for h in range(0,H):
  HC = HL.copy()
  HL = []
  for L in HC:
    HL.append(L.copy())
    L.append(h)
    HL.append(L)
Dict = {}
for count,hl in enumerate(HL):
  Dict[count] = {}
  
max = 0
for w in range(W):
  for count,hl in enumerate(HL):
    x = -1
    c = 0
    ok = True
    for h in hl:
      if x == -1:
        x = P[h][w]
        c += 1
      else:
        if x == P[h][w]:
          c += 1
        else:
          ok = False
    if ok:
      if P[h][w] in Dict[count]:
        Dict[count][P[h][w]] += c
      else:
        Dict[count][P[h][w]] = c
      if max < Dict[count][P[h][w]]:
        max = Dict[count][P[h][w]]

print(max)



      
    
    
  

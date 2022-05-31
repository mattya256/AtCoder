N = int(input())
SL = []
TL = []
for x in range(N):
  s,t = map(str,input().split())
  SL.append(s)
  TL.append(t)
for i in range(N):
  SOK = True
  TOK = True
  for j in range(N):
    if i == j:
      continue
    else:
      if SL[i] == SL[j] or SL[i] == TL[j]:
        SOK = False
      if TL[i] == TL[j] or TL[i] == SL[j]:
        TOK = False
  if SOK == False and TOK == False:
    print("No")
    exit()
print("Yes")
  
  

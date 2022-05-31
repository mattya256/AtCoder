Q = int(input())
LP = []
LM = []
LPC = 0
LMC = 0
for i in range(Q):
  t,x = map(int,input().split())
  if t == 1:
    LP.append(x)
    LPC += 1
  elif t == 2:
    LM.append(x)
    LMC += 1
  else:
    if x > LPC:
      #print(x,LPC,len(LM))
      print(LM[x-LPC-1])
    else:
      print(LP[-x])
    

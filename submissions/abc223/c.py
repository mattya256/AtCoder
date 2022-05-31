N = int(input())
lista = []
for i in range(N):
  a = [int(x) for x in input().split(" ")]
  lista.append(a)
Lcount = 0
Ltime = 0
Ltimea = 0
Llen = 0
Rcount = N -1
Rtime = 0
Rtimea = 0
while(True):
  if Lcount == Rcount:
    break
  Ltimea = Ltime + lista[Lcount][0] / lista[Lcount][1]
  Rtimea = Rtime + lista[Rcount][0] / lista[Rcount][1]
  if Ltimea < Rtimea:
    Ltime += lista[Lcount][0] / lista[Lcount][1]
    Llen += lista[Lcount][0]
    Lcount+= 1
  else:
    Rtime += lista[Rcount][0] / lista[Rcount][1]
    Rcount-= 1
  if Lcount == Rcount:
    break
a,b = lista[Rcount][0],lista[Rcount][1]
LperS = a/b
#print(Ltime,Rtime,Llen)
if Ltime < Rtime:
  X = (Rtime - Ltime)*b#“¯‚¶‚¾‚¯”R‚¦‚é‚Ü‚Å‚Ì‹——£
  XX = a - X#Žc‚è‚Ì‹——£
  Len = Llen + X + (XX/2)
else:
  X = (Ltime - Rtime)*b#“¯‚¶‚¾‚¯”R‚¦‚é‚Ü‚Å‚Ì‹——£
  XX = a - X#Žc‚è‚Ì‹——£
  Len = Llen + (XX/2)
print(Len)
    
  

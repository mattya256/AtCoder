#Ä‹A‰ñ”‘‚â‚·
import sys
sys.setrecursionlimit(10 ** 5)

numcount = 0
class Num:
  def __init__(self):
    global numcount 
    self.nc = numcount
    self.parent = None
    numcount += 1
  def checkParent(self):
    if self.parent == None:
      return self
    else:
      self.parent = self.parent.checkParent()
      return self.parent
  def setParent(self,Num):
    SP = self.checkParent()
    NP = Num.checkParent()
    if SP.nc < NP.nc:
      NP.parent = SP
    elif SP.nc > NP.nc:
      SP.parent = NP
      
class Tree:
  def __init__(self,N):
    self.N = N
    self.List = []
    self.num = Num()
  def Renketu(self):
    for l in self.List:
      if self.num.nc > l.num.nc:
        self.num.setParent(l.num)
      elif self.num.nc == l.num.nc:
        pass
      else:
        l.num.setParent(self.num)
  
Dict = {}
N,M = map(int,input().split())
for m in range(M):
  U,V = map(int,input().split())
  U,V = U-1,V-1
  if not U in Dict:
    Dict[U] = Tree(U)
  TU = Dict[U]
  if not V in Dict:
    Dict[V] = Tree(V)
  TV = Dict[V]
  TU.List.append(TV)
  TV.List.append(TU)
for i in range(N):
  if i not in Dict:
    print(0)
    exit()
  Dict[i].Renketu()
Dict1 = {}
for i in range(N):
  c = Dict[i].num.checkParent().nc

  if c in Dict1:
    Dict1[c] = [1 + Dict1[c][0],len(Dict[i].List) + Dict1[c][1]]
  else:
    Dict1[c] = [1,len(Dict[i].List)]
sum = 1
for k,v in Dict1.items():
  if v[0] == 1 or v[0] == 2:
    print(0)
    exit()
  if v[0] == v[1]//2:
    sum *= 2
    sum = sum % 998244353
  else:
    print(0)
    exit()
print(sum)
    

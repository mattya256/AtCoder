class WD():
  #keyからvalueもvalueからkeyも計算量1で
  #アクセスできる辞書
  #例 key:リンゴ,value:apple
  def __init__(self):
    self.Dict1 = {}
    self.Dict2 = {}
  def print(self):
    print("D1",self.Dict1)
    print("D2",self.Dict2)
  def set(self,value1,value2):#keyとvalueを入力
    self.Dict1[value1] = value2
    self.Dict2[value2] = value1
  def retvalue1(self,value1):
    return self.Dict1[value1]
  def retvalue2(self,value2):
    return self.Dict2[value2]
  def changevalue1(self,value1_1,value1_2):
    self.Dict2[self.Dict1[value1_1]],self.Dict2[self.Dict1[value1_2]] = self.Dict2[self.Dict1[value1_2]],self.Dict2[self.Dict1[value1_1]]
    self.Dict1[value1_1],self.Dict1[value1_2] = self.Dict1[value1_2],self.Dict1[value1_1]
  def changevalue2(self,value2_1,value2_2):
    self.Dict1[self.Dict2[value2_1]],self.Dict1[self.Dict2[value2_2]] = self.Dict1[self.Dict2[value2_2]],self.Dict1[self.Dict2[value2_1]]
    self.Dict2[value2_1],self.Dict2[value2_2] = self.Dict2[value2_2],self.Dict2[value2_1]

    
N = int(input())
P = list(map(int,input().split()))
wd = WD()
DictB = {}
for i,p in enumerate(P):
  wd.set(i+1,p)
  DictB[p] = True
List = []
for i in range(1,N+1):
  l = i
  r = wd.retvalue2(i)
  for x in reversed(range(l,r)):
    wd.changevalue1(x,x+1)
    List.append(x)
    if DictB[x]:
      DictB[x] = False
    else:
      print(-1)
      exit()
for k,v in DictB.items():
  if v and k != N:
    print(-1)
    exit()
for x in List:
  print(x)

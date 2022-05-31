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
  def set(self,value1,value2):
    #keyとvalueを入力(set(リンゴ,apple))
    self.Dict1[value1] = value2
    self.Dict2[value2] = value1
  def retvalue1(self,value1):
    #keyを入力するとvalue変換(retvalue1(リンゴ)→apple)
    return self.Dict1[value1]
  def retvalue2(self,value2):
    #valueを入力するとkey変換
    return self.Dict2[value2]
  def changevalue1(self,changed_value1,value2):
    #keyの方を変更したい時に、valueをもとに変更
    del self.Dict1[self.Dict2[value2]]
    self.Dict1[changed_value1] = value2
    self.Dict2[value2] = changed_value1
  def changevalue2(self,value1,changed_value2):
    #valueを変更したい時に、keyをもとに変更
    del self.Dict2[self.Dict1[value1]]
    self.Dict2[changed_value2] = value1
    self.Dict1[value1] = changed_value2
  def shiftvalue1(self,value1_1,value1_2):
    self.Dict2[self.Dict1[value1_1]],self.Dict2[self.Dict1[value1_2]] = self.Dict2[self.Dict1[value1_2]],self.Dict2[self.Dict1[value1_1]]
    self.Dict1[value1_1],self.Dict1[value1_2] = self.Dict1[value1_2],self.Dict1[value1_1]
  def shiftvalue2(self,value2_1,value2_2):
    self.Dict1[self.Dict2[value2_1]],self.Dict1[self.Dict2[value2_2]] = self.Dict1[self.Dict2[value2_2]],self.Dict1[self.Dict2[value2_1]]
    self.Dict2[value2_1],self.Dict2[value2_2] = self.Dict2[value2_2],self.Dict2[value2_1]

    
N,Q = map(int,input().split())
wd = WD()
for i in range(1,N+1):
  wd.set(i,i)
for q in range(Q):
  qx = int(input())
  ret = wd.retvalue2(qx)
  retp = ret + 1
  if ret == N:
    retp = ret - 1
  wd.shiftvalue1(ret,retp)
  #print(qx,ret,retp)
  #wd.print()
List = []
for x in range(1,N+1):
  List.append(wd.retvalue1(x))
print(*List)

import heapq

max = 4*10**5 + 1 #セグメントツリーの最大値、あまり大きな値にはできないため圧縮処理が必要

#セグメントツリー関連
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
queryList = []
List = []
Dict = {}
Dict2 = {}
Q = int(input())
for x in range(Q):
  query = list(map(int,input().split()))
  queryList.append(query)
  List.append(query[1])
List.sort()
count = 1
before = -1
for x in List:
  if before == x:
    continue
  else:
    Dict[x] = count
    Dict2[count] = x
    before = x
    count += 1
bit = Bit(max)
count = 0
for q in queryList:
  if q[0] == 1:
    bit.add(Dict[q[1]],1)
    count += 1
  elif q[0] == 2:
    index = bit.sum(Dict[q[1]]) + 1 - q[2]
    if index >= 1:
      print(Dict2[bit.lower_bound(index)[0]])
    else:
      print(-1)
  elif q[0] == 3:
    index = bit.sum(Dict[q[1]]-1) + q[2]
    if index <= count:
      print(Dict2[bit.lower_bound(index)[0]])
    else:
      print(-1)
    
  

  

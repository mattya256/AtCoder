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


N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

List = []
List2 = []
for x in range(N):
  heapq.heappush(List,(-1*A[x],[B[x],0]))
  List2.append(B[x])
for x in range(M):
  heapq.heappush(List,(-1*C[x]-0.1,[D[x],1]))
  List2.append(D[x])

#List2にセグメントツリーに入る値を挿入しておく。
#1,4,17,17,28のような数列を1,2,3,3,4のように小さな値に置き替える(圧縮)
List2.sort()
count = 0
before = -1
Dict = {}
for line in List2:
  if not before == line:#以前と同じならカウントを変えず、違うならカウントup
    before = line
    count += 1
  Dict[line] = count#置き替え後の数列をkey,置き替え前の数列をvalに

bit = Bit(max)
while len(List)>=1:
  x = heapq.heappop(List)
  if x[1][1] == 1:
    #要素の追加
    bit.add(Dict[x[1][0]],1)
  else:
    #x以上の最大の値を取得
    a = bit.lower_bound(bit.sum(Dict[x[1][0]]-1)+1)[0]
    #print(a,x[1][0])
    bit.add(a,-1)
    if a < Dict[x[1][0]]:
      print("No")
      exit()
    if a == max + 1:
      print("No")
      exit()
print("Yes")

"""
https://ikatakos.com/pot/programming_algorithm/data_structure/balancing_binary_search_tree/tree_free
値 x を追加 → bit.add(x,1)
値 x
を削除 → bit.add(x,－1)
k
番目の値を取得 → bit.lower_bound(k)（累積和が k
以上になる最小のindexを取得）
x
の検索 → bit.sum(x)－bit.sum(x－1)>0
x
以下の最大の値を取得 bit.lower_bound(bit.sum(x))
x
以上の最小の値を取得 bit.lower_bound(bit.sum(x－1)+1)
"""
    

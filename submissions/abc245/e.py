import heapq

max = 4*10**5 + 1 #�Z�O�����g�c���[�̍ő�l�A���܂�傫�Ȓl�ɂ͂ł��Ȃ����߈��k�������K�v

#�Z�O�����g�c���[�֘A
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
        """ �ݐϘa��x�ȏ�ɂȂ�ŏ���index�ƁA���̒��O�܂ł̗ݐϘa """
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

#List2�ɃZ�O�����g�c���[�ɓ���l��}�����Ă����B
#1,4,17,17,28�̂悤�Ȑ����1,2,3,3,4�̂悤�ɏ����Ȓl�ɒu���ւ���(���k)
List2.sort()
count = 0
before = -1
Dict = {}
for line in List2:
  if not before == line:#�ȑO�Ɠ����Ȃ�J�E���g��ς����A�Ⴄ�Ȃ�J�E���gup
    before = line
    count += 1
  Dict[line] = count#�u���ւ���̐����key,�u���ւ��O�̐����val��

bit = Bit(max)
while len(List)>=1:
  x = heapq.heappop(List)
  if x[1][1] == 1:
    #�v�f�̒ǉ�
    bit.add(Dict[x[1][0]],1)
  else:
    #x�ȏ�̍ő�̒l���擾
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
�l x ��ǉ� �� bit.add(x,1)
�l x
���폜 �� bit.add(x,�|1)
k
�Ԗڂ̒l���擾 �� bit.lower_bound(k)�i�ݐϘa�� k
�ȏ�ɂȂ�ŏ���index���擾�j
x
�̌��� �� bit.sum(x)�|bit.sum(x�|1)>0
x
�ȉ��̍ő�̒l���擾 bit.lower_bound(bit.sum(x))
x
�ȏ�̍ŏ��̒l���擾 bit.lower_bound(bit.sum(x�|1)+1)
"""
    

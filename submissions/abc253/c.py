import heapq

import sys
sys.setrecursionlimit(10 ** 5)

MAX = 4*10**5 + 1 #�Z�O�����g�c���[�̍ő�l�A���܂�傫�Ȓl�ɂ͂ł��Ȃ����߈��k�������K�v

"""
; bit = Bit(max)
; https://ikatakos.com/pot/programming_algorithm/data_structure/balancing_binary_search_tree/tree_free
; �l x ��ǉ� �� bit.add(x,1)
; �l x���폜 �� bit.add(x,�|1)
; k�Ԗڂ̒l���擾 �� bit.lower_bound(k)[0]�i�ݐϘa�� k�ȏ�ɂȂ�ŏ���index���擾�j
; x�̌��� �� bit.sum(x)�|bit.sum(x�|1)>0
; x�ȉ��̍ő�̒l���擾 bit.lower_bound(bit.sum(x))[0]
; x�ȏ�̍ŏ��̒l���擾 bit.lower_bound(bit.sum(x�|1)+1)[0]
"""

#�ŏ��l��1!!!0�͎g���Ȃ��I�I�I�I�I�I�I�I�I

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


Q = int(input())
List = []
qq = []
for _ in range(Q):
  q = list(map(int,input().split()))
  if q[0] == 1 or q[0] == 2:
    List.append(q[1])
  qq.append(q)

List.sort()
Dict = {}#���Ɓ����k
Dict2 = {}#���k������
count = 2
for l in List:
  if not l in Dict:
    Dict[l] = count
    Dict2[count] = l
    count += 1
#print(List,Dict,Dict2)

bit = Bit(MAX)

Dict3 = {} #�l�̕ێ������J�E���g
for q in qq:
  if q[0] == 1:
    if q[1] in Dict3:
      Dict3[q[1]] += 1
    else:
      Dict3[q[1]] = 1
    if q[1] in Dict:
   #   print(bit.sum(Dict[q[1]])-bit.sum(Dict[q[1]]-1))
      if not (bit.sum(Dict[q[1]])-bit.sum(Dict[q[1]]-1))>0:
        bit.add(Dict[q[1]],1)
  if q[0] == 2:
    if not q[1] in Dict3:
      Dict3[q[1]] = 0
    Dict3[q[1]] -= min(Dict3[q[1]],q[2])
    if Dict3[q[1]] == 0:
      if q[1] in Dict:
        if (bit.sum(Dict[q[1]])-bit.sum(Dict[q[1]]-1))>0:
          bit.add(Dict[q[1]],-1)
  if q[0] == 3:
    MAXMAX = bit.lower_bound(bit.sum(MAX))[0]
    MINMIN = bit.lower_bound(bit.sum(1-1)+1)[0]
    if MAXMAX in Dict2 and MINMIN in Dict2:
      print(Dict2[MAXMAX]-Dict2[MINMIN])
    else:
      pass
    #print("1",bit.lower_bound(bit.sum(MAX))[0])
    #print("2",bit.lower_bound(bit.sum(1-1)+1)[0])

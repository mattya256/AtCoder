N = int(input())
S = []
for _ in range(N):
  l = input()
  LL = []
  for i in l:
    LL.append(int(i))
  S.append(LL)
  
time = 10 ** 18
for num in range(10):#����
  Dict = {}
  for s in S:#�S�ẴX���b�g
    for i,si in enumerate(s):#�O����̗v�f
      if si == num:
        if i in Dict:
          Dict[i] += 1
        else:
          Dict[i] = 1
  MAX = 0
  for key,value in Dict.items():
    timea = key + (value-1) * 10
    MAX = max(timea,MAX)
  time = min(time,MAX)
print(time)

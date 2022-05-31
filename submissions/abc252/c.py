N = int(input())
S = []
for _ in range(N):
  l = input()
  LL = []
  for i in l:
    LL.append(int(i))
  S.append(LL)
  
time = 10 ** 18
for num in range(10):#数字
  Dict = {}
  for s in S:#全てのスロット
    for i,si in enumerate(s):#前からの要素
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

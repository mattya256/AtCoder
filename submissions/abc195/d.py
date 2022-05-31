N,M,Q = map(int,input().split())
Ni = []
for _ in range(N):
  Ni.append(list(map(int,input().split())))
Box = (list(map(int,input().split())))
for q in range(Q):
  query = list(map(int,input().split()))
  LIST = []
  for ni in Ni:
    LIST.append(ni)
  for i,box in enumerate(Box):
    if i+1 < query[0] or i+1 > query[1]:
      LIST.append([box,10 ** 7])
  LIST.sort()
  
  sum = 0
  LIST2 = []
  for list1 in LIST:
    if list1[1] == 10 ** 7:
      if len(LIST2) >= 1:
        sum += LIST2[len(LIST2)-1]
        del LIST2[len(LIST2)-1]
    else:
      LIST2.append(list1[1])
      LIST2.sort()
  print(sum)

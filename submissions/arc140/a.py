N,K = map(int,input().split())
S = input()
lS = len(S)

for i in range(1,lS+1):
  if lS % i != 0:
    continue
  DictList = [{} for _ in range(i)]
  MaxList = [0 for _ in range(i)]
  for count,s in enumerate(S):
    #print(DictList,count,i,count%i,len(DictList))
    if s in DictList[count%i]:
      DictList[count%i][s] +=1
    else:
      DictList[count%i][s] = 1
    MaxList[count%i] = max(MaxList[count%i] , DictList[count%i][s])
  #print(DictList,MaxList)
  sum = 0
  for ML in MaxList:
    sum += lS//i - ML
  #print(sum)
  if sum <= K :
    print(i)
    exit()

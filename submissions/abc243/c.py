N = int(input())
List = []
for x in range(N):
  List.append(list(map(int,input().split())))        
S = input()
Dict = {}
for i,x in enumerate(List):
  if x[1] in Dict:
    Dict[x[1]].append([x[0],S[i]])
  else:
    Dict[x[1]] = [[x[0],S[i]]]
#print(Dict)
for key,value in Dict.items():
  RR = -1
  LL = -1
  for y in value:
    if y[1] == "R":
      if RR == -1 or RR > y[0]:
        RR = y[0]
    elif y[1] == "L":
      if LL == -1 or LL < y[0]:
        LL = y[0]
  #print(RR,LL)
  if RR != -1 and LL != -1 and LL >= RR:
    print("Yes")
    exit()
print("No")
      
    
  
                

H,W = map(int,input().split())
SS = []
for _ in range(H):
  S = list(map(str,input().split()))
  SS.append(S)

List = []
for iss,ss in enumerate(SS):
  ss = ss[0]
  for iss2,s in enumerate(ss):
    if s == "o":
      List.append([iss,iss2])
print(abs(List[0][0] - List[1][0]) + abs(List[0][1] - List[1][1]))

           

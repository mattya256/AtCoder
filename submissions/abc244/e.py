import copy

N,M,K,S,T,X = map(int,input().split())
List = []
S -=1
T -=1
X -=1
for x in range(M):
  U,V = map(int,input().split())
  U -= 1
  V -= 1
  List.append([U,V])
Dict = {}
for x in range(N):
  Dict[x] = [0,0]
ND = copy.deepcopy(Dict)
Dict[S] = [1,0]
BD = copy.deepcopy(Dict)
for i in range(K):
  for x in range(N):
    BD[x] = Dict[x].copy()
  for x in range(N):
    Dict[x] = [0,0]
  for line in List:
    U = line[0]
    V = line[1]
    #print(U,V,BD[U],BD[V],BD)
    if U == X:
      Dict[U][0] = (Dict[U][0] + BD[V][1])%998244353
      Dict[U][1] = (Dict[U][1] + BD[V][0])%998244353 
    else:
      Dict[U][0] = (Dict[U][0] + BD[V][0])%998244353
      Dict[U][1] = (Dict[U][1] + BD[V][1])%998244353
    if V == X:
      Dict[V][0] = (Dict[V][0] + BD[U][1])%998244353
      Dict[V][1] = (Dict[V][1] + BD[U][0])%998244353
    else:
      Dict[V][0] = (Dict[V][0] + BD[U][0])%998244353
      Dict[V][1] = (Dict[V][1] + BD[U][1])%998244353
print(Dict[T][0])
    
  

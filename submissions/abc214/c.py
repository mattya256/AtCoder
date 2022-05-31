import heapq

#N	:頂点数
#ND	:ノードの辞書{0:[1,10],2,15]}
#S	:スタート地点
def Dijkstra(N,ND,S=0):
  MH = []#ヒープのリスト
  MD = {}#辞書
  for x in range(N):
    if x == S:
      heapq.heappush(MH,(0,x))
      MD[x] = 0
    else:
      heapq.heappush(MH,(10**18,x))
      MD[x] = 10**18
  ALD = {}
  while(True):
    min_edge = heapq.heappop(MH)[1]
    if min_edge in MD:
      for x in ND[min_edge]:
        if x[0] in MD:
          if MD[x[0]] > MD[min_edge] + x[1]:
            MD[x[0]] = MD[min_edge] + x[1]
            heapq.heappush(MH,(MD[min_edge] + x[1],x[0]))
      ALD[min_edge] = MD[min_edge]
      del MD[min_edge]
    if len(MH) == 0:
      break
  return ALD#それぞれの頂点と距離が記載されたリスト

ND = {}#{1:[2,3][5,100]}

N = int(input())

S = list(map(int,input().split()))
T = list(map(int,input().split()))

minx = -1
for x in range(N):
  s = S[x]
  t = T[x]
  nx = x + 1
  if nx == N:
    nx = 0
  if x in ND:
    ND[x].append([nx,s])
  else:
    ND[x] = [[nx,s]]
  if N in ND:
    ND[N].append([x,t])
  else:
    ND[N] = [[x,t]]
    
ALD = Dijkstra(N+1,ND,N)

for i in range(N):
  print(ALD[i])
                       

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

N,M = map(int,input().split())
for x in range(M):
  A,B,C = map(int,input().split())
  A -= 1
  B -= 1
  if A in ND:
    ND[A].append([B,C])
  else:
    ND[A] = [[B,C]]
  if B in ND:
    ND[B].append([A,C])
  else:
    ND[B] = [[A,C]]

ALD = Dijkstra(N,ND,0)
ALD2 = Dijkstra(N,ND,N-1)

for i in range(N):
  print(ALD[i] + ALD2[i])
                       

Min = -1

def check(count,List,before,sum):
  #print(before,List,sum)
  if List == []:
    global Min
    if Min == -1 or Min > sum:
      Min = sum
  for x in range(N):
    if x in List and (before == -1 or not Listaaa[before][x]):
      ListC = List.copy()
      ListC.remove(x)
      check(count+1,ListC,x,sum + A[x][count])
  
N = int(input())
A = []
for x in range(N):
  y = list(map(int,input().split()))
  A.append(y)
M = int(input())
Listaaa = []
for x in range(N):
  Listaaa.append([False] * 10)
for x in range(M):
  x,y = map(int,input().split())
  Listaaa[x-1][y-1] = Listaaa[y-1][x-1] = True
List = []
for x in range(N):
  List.append(x)
check(0,List,-1,0)
print(Min)


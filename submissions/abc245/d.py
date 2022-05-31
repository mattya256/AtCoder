N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

BD = {}
mx = M
count = 0
while(True):
  count2 = 0
  min = N + M - count
  Cx = C[min]
  while(True):
    nx = N - (count - count2)
    mx = M - count2
    if count == count2:
      break
    if 0 <= nx <= N and 0 <= mx <= M:
      Cx -= A[nx] * BD[mx] 
    count2 += 1
    #print(Cx,A[nx],BD[mx],nx,mx,min,C[min]) 
  BD[mx] = int(int(Cx)/int(A[nx]))
  #print(count,count2,mx,Cx,BD[mx])
  if mx == 0:
    break
  count += 1
for x in range(M+1):
  print(BD[x])
            

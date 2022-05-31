N,M,K = map(int,input().split())

L = [[0 for _ in range(N*M)] for _ in range(N)] 
for i in range(M):
  if i < K :
  	L[0][i] = 1

for i in range(0,N-1):
  for j in range(N * M):
    for k in range(1,M+1):
      if j + k < K:
        L[i+1][j+k] += L[i][j]
        L[i+1][j+k] %= 998244353
sum = 0
for x in range(N*M):
  sum += L[N-1][x]
  sum %= 998244353
print(sum)
  
    

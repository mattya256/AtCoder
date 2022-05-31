N,M,K = map(int,input().split())

MAP = [[0 for _ in range(M)] for _ in range(N)]
sum = 0
for i,m in enumerate(MAP[0]):
  MAP[0][i] = 1
  sum += 1
sum2 = sum
for i in range(1,N):
  for j in range(0,M):
    if j-K >= 0:
      MAP[i][j-K] += sum
      MAP[i][j-K] = MAP[i][j-K]%998244353
    if j < M:
      sum -= MAP[i-1][j]
  List = []
  count1 = M-1
  for ii in range(M):
    List.append(count1)
    count1-=1
  for j in List:
    if j+K < M :
      MAP[i][j+K] += sum2
      MAP[i][j+K] = MAP[i][j+K]%998244353
    if j > 0:
      sum2 -= MAP[i-1][j]
    if K == 0:
      MAP[i][j] -= MAP[i-1][j]
  sum = 0
  for j in range(M):
    sum += MAP[i][j]
    sum = sum%998244353
  sum2 = sum%998244353

print(sum %998244353)

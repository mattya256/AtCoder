N,K = map(int,input().split())
MD = {}

if K <= 2 and N > K:
  print(0)
  exit()
if N == 1:
  print(K)
  exit()
elif N == 2:
  print(K*(K-1))
  exit()
else:
  sum = K * (K-1)
  N = N-2
  count = 2
  MD[1] = (K-2)%(10**9 + 7)
  while(True):
    if 2 ** (count-1) > N:
      break
    MD[count] = (MD[count-1]**2)%(10**9 + 7)
    count += 1
  #print(MD)
  while(True):
    if 2 ** (count-1) <= N:
      sum *= MD[count]
      sum = sum %(10**9 + 7)
      N -= 2 ** (count-1)
    count -= 1
    #print(count,sum,N)
    if count<=0:
      break
print(sum)

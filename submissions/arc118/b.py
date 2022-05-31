K,N,M = map(int,input().split())
A = list(map(int,input().split()))
dev = M/N

BB = [[-1,-1] for _ in range(K)]
BBint = [-1 for _ in range(K)]

sum = 0
for k in range(K):
  BBint[k] = A[k]*M//N
  BB[k] = [BBint[k] * N - A[k] * M,k]
  sum += BBint[k]
BB.sort()
sum -= M
#print(BB,BBint,sum)
if sum > 0:
  count = 0
  while(sum > 0):
    List = BB[count]
    BBint[List[1]] -= 1
    count += 1
    sum -= 1
elif sum < 0:
  count = 0
  while(sum < 0):
    List = BB[count]
    BBint[List[1]] += 1
    count += 1
    sum += 1

print(*BBint)
  

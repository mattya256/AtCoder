N,K,X = map(int,input().split())
A = list(map(int,input().split()))

count = 0
sum = 0
for i,a in enumerate(A):
  sum += a
  count += int(a/X)
  a = a % X
  A[i] = a
if count >= K:
  print(sum - K*X)
  exit()
Minus = count * X
list.sort(A,reverse = True)
for a in A:
  count += 1
  Minus += a
  if count == K:
    break
print(sum -Minus)
  
    

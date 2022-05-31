X = int(input())
A = [1] * 5
B = [1] * 5
for aaa in range(X-1):
  for x in range(5):
    if 4 > x > 0:
      A[x] = (B[x-1] + B[x] + B[x+1])%998244353
    elif x == 0:
      A[x] = (B[x] + B[x+1])%998244353
    else:
      A[x] = (B[x-1] + B[x-1] + B[x])%998244353
  B = A.copy()
sum = 0
for i,a in enumerate(A):
  if i == 4:
    sum += a
    sum = sum%998244353
  else:
    sum += a*2
    sum = sum%998244353
print(sum)
  

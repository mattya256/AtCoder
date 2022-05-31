N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
CI = 0
for i in range(N):
  if A[i] == B[i]:
    CI += 1
CJ = 0
for i in range(N):
  for j in range(N):
    if i != j:
      if A[i] == B [j]:
        CJ += 1
print(CI)
print(CJ)
  

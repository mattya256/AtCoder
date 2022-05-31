N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
sum = 0
for x in range(N):
  sum += abs(A[x] - B[x])
print(sum)

N,W = map(int,input().split())
A = list(map(int,input().split()))
List = [0 for _ in range(3 * 10 ** 6 + 1)]
for i in range(N):
  for j in range(i):
    for k in range(j):
      List[A[i]+A[j]+A[k]] += 1
    List[A[i]+A[j]] += 1
  List[A[i]] += 1
sum = 0
for i in range(W+1):
  if List[i] != 0:
    sum += 1
print(sum)

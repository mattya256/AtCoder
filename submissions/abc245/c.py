N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


AA = -1
BB = -1
for x in range(N):
  AA2 = -1
  BB2 = -1
  if AA != -1:
    if abs(AA-A[x]) <= K:
      #print("a")
      AA2 = A[x]
    if abs(AA-B[x]) <= K:
      #print("b")
      BB2 = B[x]
  if BB != -1:
    if abs(BB-A[x]) <= K:
      #print("c")
      AA2 = A[x]
    if abs(BB-B[x]) <= K:
      #print("d")
      BB2 = B[x]
  if x == 0:
    AA2 = A[x]
    BB2 = B[x]
  AA = AA2
  BB = BB2
  #print(AA,BB)
if AA!=-1 or BB != -1:
  print("Yes")
else:
  print("No")

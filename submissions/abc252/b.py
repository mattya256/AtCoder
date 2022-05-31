N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
List = []
MAX = 0
for a in A:
  MAX = max(MAX,a)
for i,a in enumerate(A):
  if a == MAX:
    List.append(i+1)
for i in List:
  for b in B:
    if i == b:
      print("Yes")
      exit()
print("No")

  

A,B,K = map(int,input().split())
count = 0
while(True):
  if A >= B:
    break
  count += 1
  A = A * K
  if A >= B:
    break
print(count)

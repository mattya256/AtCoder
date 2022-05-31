N = int(input())
A = list(map(int,input().split()))
MAXa = 0
SUMAX = 0
sum = 0
for i,a in enumerate(A):
  if MAXa < a:
    SUMAX = SUMAX + a + (a-MAXa)
    if i == 0:
      sum = a * 2
    else:
      sum += (i) * (a-MAXa) + SUMAX 
    MAXa = a
  else:
    SUMAX = SUMAX + a
    sum += SUMAX
  print(sum)

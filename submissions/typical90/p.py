N = int(input())
A,B,C = map(int,input().split())
if A < B:
  A,B = B,A
if A < C:
  A,C = C,A
if B < C:
  B,C = C,B
  
MAXA = int(N/A)
MAXB = int(N/B)
min = 10000
for a in reversed(range(0,MAXA+1)):
  for b in reversed(range(0,MAXB+1)):
    nokori = N - A*a
    nokori -= B*b

    if (nokori > 0 and nokori % C == 0) or nokori == 0:
      if min > (a + b + int(nokori/C)):
        min = (a + b + int(nokori/C))
print(min)

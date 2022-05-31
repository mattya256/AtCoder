import math

x = int(input())
y = []
for i in range(x):
  zzz = []
  zzz = [int(xx) for xx in input().split()]
  y.append(zzz)
max = 0
for a in y:
  a1,a2 = a[0],a[1]
  for b in y:
    b1,b2 = b[0],b[1]
    yoko = abs(a1 - b1)
    tate = abs(a2 - b2)
    nagasa = yoko * yoko + tate * tate
    if max < nagasa:
      max = nagasa
print(math.sqrt(max))

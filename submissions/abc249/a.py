A,B,C,D,E,F,X = map(int,input().split())

a = A
c = C
d = D
f = F
TT = AA = 0
for i in range(X):
  if a > 0:
    TT += B
    a -= 1
  else:
    c -= 1
    if c == 0:
      c = C
      a = A
  if d > 0:
    AA += E
    d -= 1
  else:
    f -= 1
    if f == 0:
      f = F
      d = D
if TT == AA:
  print("Draw")
elif TT > AA:
  print("Takahashi")
else:
  print("Aoki")
  

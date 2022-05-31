from decimal import Decimal

N,X = map(int,input().split())
S = input()
count = 0
for s in S:
  if X > ((10**18)/2)+1 and s != "U":
    count += 1
  elif s == "U":
    if count > 0:
      count -= 1
    else:
      X = Decimal(X)
      X = int(X/2)
  elif s == "L":
    X *= 2 
  elif s == "R":
    X *= 2 
    X += 1
  #print(count)
print(X)


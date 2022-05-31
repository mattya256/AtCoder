import math

def check(intA):
  if intA == 1:
    return True
  if intA == 2:
    return False
  Max = int(math.sqrt(intA)) + 1
  for x in range(2,Max+1):
    if intA%x == 0:
      return True
  return False

inputx = [int(x) for x in input().split(" ")]
A = inputx[0]
B = inputx[1]
C = inputx[2]
D = inputx[3]
for x in range(A,B+1):
  AokiWin = False
  for y in range(C,D+1):
    if not check(x+y):
      AokiWin = True
  if not AokiWin:
    print("Takahashi")
    exit()
print("Aoki")

    

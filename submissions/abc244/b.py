N = int(input())
T = input()
Count = 0
x = [0,0]
L = [[0,1],[-1,0],[0,-1],[1,0]]
for t in T:
  if t == "S":
    x[0] += L[Count%4][0]
    x[1] += L[Count%4][1]
  if t == "R":
    Count += 1
print(x[1],x[0])

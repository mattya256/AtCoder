H,W = map(int,input().split())
S = []
for x in range(H):
  S.append(input())
count = 0
sum = 0
while(True):
  color = "."
  for x in range(count+1):
    y = count - x
    if W > x and H > y:
      if color == ".":
      	color = S[y][x]
      else:
        if (not S[y][x] == ".") and (not color == S[y][x]):
          print(0)
          exit()
  count += 1
  #print(count,color)
  if color == ".":
    sum += 1
  if count >= W + H - 1:
    break
print(pow(2,sum,998244353))
      
  

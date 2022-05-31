N,A,B = map(int,input().split())
countA = 0
for y in range(A*N):
  Str = ""
  aa = (countA // A)%2 
  countB = 0
  for x in range(B*N):
    bb = (countB //B) % 2
    if (aa + bb) % 2 == 0:
      Str += "."
    else:
      Str += "#"
    countB += 1
  countA += 1
  print(Str)
    

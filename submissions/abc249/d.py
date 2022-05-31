N = int(input())
A = list(map(int,input().split()))
Dict = {}
for a in A:
  if a in Dict:
    Dict[a] += 1
  else:
    Dict[a] = 1

count = 0
for x in range(1,2 * 10**5 + 5):
  y = 0
  while(True):
    y += 1
    if y ** 2 > x:
      break
    if x % y == 0:
      z = int(x/y)
      if x in Dict and y in Dict and z in Dict:
       
        if z == y:
          count += Dict[x] * Dict[y] * Dict[z]
        else:
          count += Dict[x] * Dict[y] * Dict[z] * 2
print(count)
    

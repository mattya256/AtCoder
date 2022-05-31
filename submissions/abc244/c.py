N = int(input())
N = N*2 + 1
count = 0
dict = {}
for x in range(1,N+1):
  dict[x] = False
while(True):
  for x,y in dict.items():
    if y == False:
      print(x,flush = True)
      dict[x] = True
      break
  count += 1
  if count == N:
    break
  a = int(input())
  dict[a] = True
  count += 1

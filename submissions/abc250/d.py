N = int(input())
SL = []#‘f”ƒŠƒXƒg
NSL = [False for _ in range(10 ** 6 + 1)]
count = 2

while(True):
  if NSL[count]:
    pass
  else:
    SL.append(count)
    count2 = count
    while(True):
      NSL[count2] = True
      count2 += count
      if count2 > 10 ** 6:
        break
  count += 1
  if count > 10 ** 6:
    break

Dict = {}
sum = 0
for q in SL:
  for p in SL:
    count += 1
    if p >= q:
      break
    a = p * (q ** 3)
    if a < N + 1:
      sum += 1 
    else:
      break

print(sum)
    
  
  

N = int(input())
S = input()
T = input()
LIST = [0 for _ in range(N)]
countLIST = [0 for _ in range(N)]
count = 0

for x in range(N):
  s = int(S[x])
  t = int(T[x])
  if s == 1 and t == 1:
    LIST[x] = 1
  if s == 0 and t == 0:
    LIST[x] = 2
  if s == 1 and t == 0:
    LIST[x] = 3
    count += 1
  if s == 0 and t == 1:
    LIST[x] = 4
    count -= 1
  countLIST[x] = count
if countLIST[x] != 0:
  print(-1)
  exit()
#print(countLIST,LIST)
def check(left,right,turn,LIST):
  sum = 0
  count = 0
  while(True):
    if turn == True:
      x = right 
    else:
      x = left 
    #print(left,right,x,LIST[x],count,sum)
    if LIST[x] == 1:
      pass
    elif LIST[x] == 2:
      if count != 0:
        sum += 1
    elif LIST[x] == 3:
      count += 1
    else:
      count -= 1
      sum += 1
    if right == left and count == 0:
      return sum
    if turn == True:
      right -= 1
    else:
      left += 1

left = 0
count = 0
CHECK = 0
sum = 0
for x in range(N):
  if countLIST[x] > 0:
    CHECK = 1
  elif countLIST[x] < 0:
    CHECK = -1
  if countLIST[x] == 0 and CHECK != 0:
    if CHECK == 1:
      turn = False
    else:
      turn = True
    sum += check(left,x,turn,LIST)
    left = x+1
    CHECK = 0

print(sum)
  

  

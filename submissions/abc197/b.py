def change(list):
  intlist = []
  for str in list:
    if str == ".":
      intlist.extend([0]) 
    else:
      intlist.extend([1])
  return intlist

H,W,X,Y = [int(number) for number in input().split(" ")]
X -= 1
Y -= 1
mass = []
sum = 1
for i in range(H):
  mass.append(change(list(input())))
for count in range(4):
  go=0
  if count%2==1:
    countgo=1
  else:
    countgo=-1
  while True:
    go += countgo
    if count < 2:
      if 0<=X+go<H and mass[X+go][Y]==0:
        sum +=1
      else:
        break
    else:
      if 0<=Y+go<W and mass[X][Y+go]==0:
        sum +=1
      else:
        break
print(sum)

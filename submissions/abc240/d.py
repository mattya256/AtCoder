N = int(input())
a = [int(x) for x in input().split(" ")]

BOX = []
count = 0
count_B = 0
for i in range(1,N+1):
  #print(a[i-1])
  if len(BOX) > 0 and BOX[count-1][0] == a[i-1]:
    if BOX[count-1][1] == a[i-1]-1:
      del BOX[count-1]
      count_B -= a[i-1]-1
      count -=1
    else:
      BOX[count-1][1] = BOX[count-1][1] + 1
      count_B += 1
  else:
    BOX.append([a[i-1],1])
    count += 1
    count_B += 1
  print(count_B)
  #print(BOX)

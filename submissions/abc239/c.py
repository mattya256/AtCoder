inputx = [int(x) for x in input().split(" ")]
x1 = inputx[0]
y1 = inputx[1]
x2 = inputx[2]
y2 = inputx[3]

list_PM = [+1,-1]
for a in list_PM:
  for b in list_PM:
    for c in range(1,3):
      for a2 in list_PM:
        for b2 in list_PM:
          for c2 in range(1,3):
            x11 = x1 + c * a
            y11 = y1 + (3 - c) * b
            x21 = x2 + c2 * a2
            y21 = y2 + (3 - c2) * b2
            if x11 == x21 and y11 == y21:
              print("Yes")
              exit()
print("No")
    

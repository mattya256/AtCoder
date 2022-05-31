x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
z = [int(x) for x in input().split()]

for zz in z:
  n=True
  for count,yy in enumerate(y):
    if zz == yy:
      del y[count]
      n=False
      break
  if n:
    print("No")
    exit()
print("Yes")

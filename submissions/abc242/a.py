x=[int(x) for x in input().split()]
a =x[0]
b=x[1]
c=x[2]
x=x[3]

if x<=a:
  print(1)
elif x<=b:
  print(c/(b-a))
else:
  print(0)

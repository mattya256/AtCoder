x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

x = [-1,-1]
y = [-1,-1]

x[0] = x1
y[0] = y1
x0 = 1
y0 = 1
if x2 != x[0]:
  x[1] = x2
else:
  x0 += 1
if y2 != y[0]:
  y[1] = y2
else:
  y0 += 1
if x3 != x[0]:
  x[1] = x3
else:
  x0 += 1
if y3 != y[0]:
  y[1] = y3
else:
  y0 += 1
Str = ""
if x0 == 1:
  Str += str(x[0])
else:
  Str += str(x[1])
Str += " "
if y0 == 1:
  Str += str(y[0])
else:
  Str += str(y[1])
print(Str)

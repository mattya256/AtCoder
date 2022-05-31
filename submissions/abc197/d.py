import math

N = int(input())
x0,y0 = map(int,input().split())
x1,y1 = map(int,input().split())

xc = (x0+x1)/2
yc = (y0+y1)/2

x0,y0 = x0 - xc ,y0 - yc
x1,y1 = x1 - xc, y1 - yc

len0 = math.sqrt(x0 ** 2 + y0 ** 2)
x0l , y0l = x0/len0,y0/len0
sinx0l = math.degrees(math.asin(x0l))
if y0l < 0:
  if x0l < 0:
    sinx0l = -180 - sinx0l
  else:
    sinx0l = 180 - sinx0l
sinN = math.sin(math.radians(-(360/N) + sinx0l))
cosN = math.cos(math.radians(-(360/N) + sinx0l))
#print(-(360/N) + sinx0l)
#print(sinN * len0 , xc,cosN * len0, yc)
print(sinN * len0 + xc,cosN * len0+ yc)

import math

L,R = map(int,input().split())
for x in range(10**18):
  for y in range(x+1):
    LL = L + y
    RR = R - (x-y)
    #print(LL,RR,x,y)
    if math.gcd(LL,RR) == 1:
      print(RR-LL)
      exit()

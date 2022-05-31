def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

xxx= list(map(int,input().split()))
xxx.sort()
A=xxx[0]
B=xxx[1]
C=xxx[2]
if A == C:
  print(A)
  exit()
AA = A
CC = C
while(True):
  if CC-AA>0:
    CC = CC-AA
    if CC < AA:
      CC,AA = AA,CC
  else:
    break
  if AA < 1000000:
    break
List = make_divisors(AA)
for x in List[::-1]:
  if x == 1:
    pass
  elif A % x == 0 and C % x == 0 and B % x == 0:
    print(int(A/x + C/x + B/x) -3)
    exit()
print(A-1 + B-1 + C-1)
    

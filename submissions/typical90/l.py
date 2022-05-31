def check(a):
  Lista = []
  Listb = [a]
  for x in range(2,a):
    if x * x > a:
      break
    else:
      if a%x == 0:
        Lista.append(x)
        Listb.append(int(a/x))
        a = int(a/x)
  Lista.extend(Listb[::-1])
  return Lista
        

A,B = map(int,input().split())
if A < B:
  A,B = B,A
C = 0
AA = A
BB = B
while(True):
  if AA-BB > 0:
    AA = AA-B
    if AA < BB:
      AA,BB = BB,AA
  if BB < 10000:
    break
  else:
    break
List = []
if AA%BB == 0:
  List = [BB]
else:
  List = check(BB)
sum = 1
for x in List[::-1]:
  while(True):
    if A%x == 0 and B%x == 0 and x != 1:
      sum *= int(x)
      A = int(A/x)
      B = int(B/x)
      sum = int(sum)
    else:
      break
  if sum > 10 ** 18:
    break
x = A * B * sum
if x > 10 ** 18:
  print("Large")
else:
  print(int(x))
    
  

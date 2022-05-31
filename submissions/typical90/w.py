def check(N,count):
  #print(N)
  for i in range(2,N):
    if i * i > N :
      break
    if N % i == 0:
      count += 1
      return check(int(N/i),count)
  return count

N = int(input())
b = check(N,0) + 1
if b == 1:
  print(0)
  exit()
a = 1
#print("b",b)
while(True):
  if 2 ** a >= b:
    print(a)
    exit()
  a += 1

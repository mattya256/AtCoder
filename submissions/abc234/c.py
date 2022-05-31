K = int(input())
x = 2
Str = ""
while(True):
  a = K % 2
  if a == 0:
    Str = "0" + Str
  else:
    Str = "2" + Str 
  K = K//2
  #print(K,a,Str)
  if K == 0:
    break
print(Str)

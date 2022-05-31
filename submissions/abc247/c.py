N = int(input())
Str = []
for i in range(1,N+1):
  Str = Str + [str(i)] + Str
Strout = ""
for x in Str:
  Strout += x + " "
print(Strout[:-1])
  

splitnum = input().split(" ")
s = int(splitnum[0])
max = int(splitnum[1])
count = 0  
x=y=z=-1
if max/10000 <= s <= max/1000:
  for a in range(0,s+1):
    for b in range(0,s+1-a):
      c=s-a-b
      if 10000*a+5000*b+1000*c==max:
        x=a
        y=b
        z=c
print(str(x)+" " +str(y)+" "+str(z))

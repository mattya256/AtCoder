H,W= map(int,input().split())
R,C= map(int,input().split())
sum = 0
if not R == 1:
  sum += 1
if not R == H:
  sum += 1
if not C == 1:
  sum += 1
if not C == W:
  sum += 1
print(sum)
  

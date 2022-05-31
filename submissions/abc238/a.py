n = int(input())
if n < 100:
  if 2 ** n > n ** 2:
    print("Yes")
    exit()
  else:
    print("No")
    exit()
for x in range(100,n+1):
  if 2 ** x > x ** 2:
    print("Yes")
    exit()
print("No")

n = input()
a = input().split(" ")
max = 10**9
for strobj in a:
  num = int(strobj)
  count = 0
  while True:
    if num%2==0:
      num /= 2
      count +=1
    else:
      if max>count:
      	max = count
      break
print(max)

N = int(input())
S = input()
AC = 0
CC = 0
Z = 0
List = []
for s in S:
  if Z == 0:
    AC = RC = 0
  if Z == 3 and (s =='A' or s == 'R'):
    List.append(min(AC,CC))
    Z = AC = CC = 0
  if s == 'A':
    if Z == 1:
      AC += 1
    else:
      Z = 1
      AC = 1
  elif s == 'R':
    if Z == 1:
      Z = 2
    else:
      Z = 0
  elif s == 'C':
    if Z == 2:
      Z = 3
      CC = 1
    elif Z == 3:
      CC += 1
    else :
      Z = 0
if Z == 3 :
    List.append(min(AC,CC))
sum = 0
for i in List:
  sum += i
#print(List)
print(min(sum,len(List)*2))
    
  
  

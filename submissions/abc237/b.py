H,W = [int(x) for x in input().split(" ")]
listb = []
for j in range(1,H+1):
  lista = [int(y) for y in input().split(" ")]
  #for i in range(1,W+1):
  listb.append(lista)
count = 0

listx = []
for listbb in listb:
  counta = 0  
  for youso in listbb:
    if count == 0:
      listx.append([youso])
    else:
      listx[counta].append(youso)
    counta += 1
  count += 1

Stringf = ""
for a in listx:
  String = ""
  count = 0
  for b in a:
    if not count == 0:
      String += " "
    String += str(b)
    count += 1
  Stringf += String +"\n"
print(Stringf)
    
  



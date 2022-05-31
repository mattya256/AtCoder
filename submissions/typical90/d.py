H , W = map(int,input().split())
lista = []
for i in range(H):
  lista.append(list(map(int,input().split())))

dicti = {}
for i in range(H):
  sum = 0
  for j in range(W):
    sum += lista[i][j]
  dicti[i] = sum

dictj = {}
for j in range(W):
  sum = 0
  for i in range(H):
    sum += lista[i][j]
  dictj[j] = sum

listc = []
for i in range(H):
  listb = []
  for j in range(W):
    sum = 0
    sum = dicti[i] + dictj[j] - lista[i][j]
    listc.append(sum)
  listb.append(listc)

for x in listb:
  stra = ""
  for y in x:
    stra += str(y) + " "
  print(stra[:-1])
    

N = int(input())
lista = [int(x) for x in input().split(" ")]
lista.sort()
count = 0
before = -1
for x in lista:
  if x == before:
    pass
  else:
    count +=1
  before = x
print(count)

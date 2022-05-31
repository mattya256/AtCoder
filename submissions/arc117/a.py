a,b = [int(number) for number in input().split(" ")]
list = []
if a > b:
  sa = sum([number for number in range(1,a-b+1)])
  lista = [number for number in range(1,a)]
  listb = [number for number in range(-(a-b+1),-a,-1)]
  listc = [2*a,-2*a-sa]
  lista.extend(listb)
  lista.extend(listc)
else:
  sa = sum([number for number in range(1,b-a+1)])
  lista = [number for number in range(b-a+1,b)]
  listb = [number for number in range(-1,-b,-1)]
  listc = [2*b+sa,-2*b]
  lista.extend(listb)
  lista.extend(listc)
string = ""
for number in lista:
  string += str(number)+ " "
print(string)
  

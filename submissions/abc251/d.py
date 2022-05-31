List = []
for i in range(1,101):
  List.append(i)
  List.append(i*10**2)
  List.append(i*10**4)
print(len(List))
print(*List)

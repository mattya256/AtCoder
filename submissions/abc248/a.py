S = input()
List = []
for s in S:
  List.append(int(s))
for x in range(10):
  if x not in List:
    print(x)
  

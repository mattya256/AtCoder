N,D = map(int,input().split())

Dict = {}
List = []
for n in range(N):
  L,R = map(int,input().split())
  if L in Dict:
    if Dict[L] > R:
      Dict[L] = R
  else:
    Dict[L] = R
  List.append(L)
List.sort()
min = 10**10
count = 0
breaka = -1
for l in List:
  if l == min:
    count += 1
    breaka = min + D -1
    min = 10 ** 10
  elif l > min:
    count += 1
    breaka = min + D - 1
    min = 10 ** 10
    r = Dict[l]
    if r < min and l > breaka:
      min = r
  else:
    r = Dict[l]
    if r < min and l > breaka:
      min = r
if min != 10**10:
  count += 1
print(count)
  
  

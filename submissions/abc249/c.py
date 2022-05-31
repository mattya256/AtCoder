import copy

N,K = map(int,input().split())
List = []
for k in range(N):
  List.append(input())

KA = [""]
for x in range(N):
  KAC = copy.deepcopy(KA)
  KA = []
  for kac in KAC:
    KA.append(kac)
    KA.append(kac + "," + str(x))

ALL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

Dict = {}

for ka in KA:
  if ka != "":
    kal = ka.split(",")
    for s in kal:
      if s == "":
        continue
      s = int(s)
      for al in ALL:
        if al in List[s]:
          if ka in Dict and al in Dict[ka]:
            Dict[ka][al] += 1
          else:
            if ka in Dict:
              pass
            else:
              Dict[ka] = {}
            Dict[ka][al] = 1
max = 0
for key,value in Dict.items():
  count = 0
  for key2,value2 in value.items():
    if value2 == K:
      count += 1
  if max < count:
    max = count 
print(max)
  

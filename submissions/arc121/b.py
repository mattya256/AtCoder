N = int(input())
R = G = B = 0
DICT = {}
LIST = []
for _ in range(2 * N):
  a,c = map(str,input().split())
  a = int(a)
  if c == "R":
    c = 0
  elif c == "B":
    c = 1
  else:
    c = 2
  if c in DICT:
    DICT[c] += 1
  else:
    DICT[c] = 1
  LIST.append([a,c])
check = True
ONELIST = []
TWO = -1
for k in [0,1,2]:
  if k in DICT:
    v = DICT[k]
  else:
    v = 0
  if v % 2 == 0:
    TWO = k
    pass
  else:
    ONELIST.append(k)
    check = False
if check:
  print(0)
  exit()

colorLIST = [0,1,2]
LIST.sort()
DICT2 = {"01":10**18,"02":10**18,"12":10**18}
MAX = [-10 ** 18 for _ in range(3)]
for l in LIST:
  MAX[l[1]] = l[0]
  l = l[1]
  for color in colorLIST:
    if l != color:
      if l > color:
        a,b = color,l
      else:
        a,b = l,color
      aaa = abs(MAX[a] - MAX[b])
      DICT2[str(a) + str(b)] = min(aaa,DICT2[str(a) + str(b)])

if ONELIST[0] > ONELIST[1]:
  ONELIST[0],ONELIST[1] = ONELIST[1],ONELIST[0]
xxx = DICT2[str(ONELIST[0]) + str(ONELIST[1])]
a , b = ONELIST[0] , TWO
if a > b:
  a,b = b,a
yyy = DICT2[str(a) + str(b)]
b,c = ONELIST[1] , TWO
if b > c:
  b,c = c,b
yyy += DICT2[str(b) + str(c)]
print(min(xxx,yyy))

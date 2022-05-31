S = list(map(str,input().split()))
T = list(map(str,input().split()))
dict = {}
for i in range(3):
  for j in range(3):
    for k in range(3):
      if i!=j and i!= k and j != k:
        dict[str(i)+str(j)+str(k)]=False
color = {"R":"0","G":"1","B":"2"}
BD = dict.copy()
BD[color[S[0]],color[S[1]],color[S[2]]] = True
for x in range(2):
  ND = dict.copy()
  for x,y in BD.items():
    if y == True:
      a = (x[0])
      b = (x[1])
      c = (x[2])
      ND[b+a+c] = ND[a+c+b] = ND[c+b+a] = True
  BD = ND
if BD[color[T[0]]+color[T[1]]+color[T[2]]] == True:
  print("Yes")
else:
  print("No")
  

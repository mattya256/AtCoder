S = input()
L = False
SS = False

for s in S:
  if s.isupper():
    L = True
  if s.islower():
    SS = True

for x in range(len(S)):
  for y in range(len(S)):
    if x == y:
      pass
    else:
      if S[x] == S[y]:
        print("No")
        exit()
if SS and L:
  print("Yes")
else:
  print("No")

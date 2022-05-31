import re

N = int(input())
S = input()

Str = ""
beforeB = False
for x in S:
  if x == "C":
    if beforeB:
      Str += "B"
      beforeB = False
    Str += x
  elif x == "A":
    Str += x
  elif x == "B":
    if beforeB == True:
      Str += "A"
      beforeB = False
    else:
      beforeB = True
if beforeB:
  Str += "B"
print(Str)
  
  

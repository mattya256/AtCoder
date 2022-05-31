V,A,B,C = map(int,input().split())
count = 0
while(True):
  if count % 3 == 0:
    V -= A
  elif count % 3 == 1:
    V -= B
  elif count % 3 == 2:
    V -= C
  if V < 0:
    if count % 3 == 0:
      print("F")
      exit()
    elif count % 3 == 1:
      print("M")
      exit()
    elif count % 3 == 2:
      print("T")
      exit()
  count += 1

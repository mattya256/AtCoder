N = int(input())
S = input()
List = [0] * N
List2 = [0] * N
for i in range(7):
  a = 0
  for j in reversed(range(N)):
    if i == 0:
      if S[j] == "r":
        a += 1
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==1:
      if S[j] == "e":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==2:
      if S[j] == "d":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==3:
      if S[j] == "o":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==4:
      if S[j] == "c":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==5:
      if S[j] == "t":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
    elif i ==6:
      if S[j] == "a":
        a += List2[j]
        a = a % (10**9 + 7)
      List[j] = a
  List2 = List
print(a)
        
    

import math

loop = {0:1}
for i in range(1,10 ** 6):
  loop[i] = (loop[i-1] * 26)%998244353
T = int(input())
dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
for i in range(T):
  OK = True
  N = int(input())
  S = (input())
  sum = 0
  for count in range(math.ceil(N/2)):
    #if S[count] < S[N-count-1]:
    sum = (sum + dic[S[count]]*loop[math.ceil(N/2)-count-1])%998244353
    if S[count] < S[N-count-1]:
      OK = True
    elif S[count] == S[N-count-1]:
      pass
    else:
      OK = False
    #else:
     # print(sum,loop[math.ceil(N/2)-count-1],[math.ceil(N/2)-count-1], dic[S[N-count-1]],S[N-count-1],N-count-1)
      #sum = sum + dic[S[N-count-1]]*loop[math.ceil(N/2)-count-1]%99824435
  if OK:
    pass
    sum = (sum + 1)%998244353
  print(sum) 

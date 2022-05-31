T = int(input())
for _ in range(T):
  N,A,B,X,Y,Z = map(int,input().split())
  if Y/A > Z/B:
    A,B = B,A
    Y,Z = Z,Y
  sum = 0
  NA = N // A
  NB = A - 1
  Y = min([Y,A*X])
  Z = min([Z,B*X])
  Min = -1
  if NA >= NB:
    for bb in range(A-1 + 1):
      NN = N - bb * B
      aa = NN // A
      NN = NN % A
      sum_x = sum + bb * Z + aa * Y + NN * X
      if Min == -1 or sum_x < Min:
        Min = sum_x
        #print("b:",aa,bb,NN,sum_x,NA,NB)
  else:
    for aa in range(NA + 1):
      NN = N - aa * A
      bb = NN // B
      NN = NN % B
      sum_x = sum + bb * Z + aa * Y + NN * X
      if Min == -1 or sum_x < Min:
        Min = sum_x
        #print("a:",aa,bb,NN,sum_x,NA,NB)
  print(Min)
  continue

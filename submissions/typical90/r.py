N,Q = map(int,input().split())
A = list(map(int,input().split()))
count = 0
for i in range(Q):
  """
  Str = ""
  for j in range(N):
    Str += str(A[(count+j)%N]) +","
  print(Str)
  """
  T,x,y = map(int,input().split())
  if T == 1:
    save = A[(count+x-1)%N]
    A[(count+x-1)%N] = A[(count+y-1)%N]
    A[(count+y-1)%N] = save
  elif T == 2:
    count -= 1
  elif T == 3:
    print(A[(count+x-1)%N])

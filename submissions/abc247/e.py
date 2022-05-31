N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
PX = -1 #ÅŒã‚ÌX‚ÌˆÊ’u 
PY = -1 #ÅŒã‚ÌY‚ÌˆÊ’u
PP = -1 #ÅŒã‚Ì‚Ç‚¿‚ç‚Å‚à‚È‚¢ˆÊ’u
sum = 0
for i in range(N):
  #print("i",i,"PX",PX,"PY",PY,"PP",PP)
  #print("sum",sum,"X",X,"Y",Y,"A",A[i])
  if A[i] > X or A[i] < Y:
    PX = -1
    PY = -1
    PP = -1
  elif PP == -1:
    PP = i
  if A[i] == X:
    PX = i
  if A[i] == Y:
    PY = i
  if PX != -1 and PY != -1 and PP != -1:
    if PX < PY:
      sum += PX - PP + 1
    else:
      sum += PY - PP + 1
print(sum)
  

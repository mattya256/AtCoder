N = int(input())
A = list(map(int,input().split()))

List = [[0 for _ in range(2)] for _ in range(N+1)]

before = True
a = 0 #前回あげた今回あげた
b = 0 #前回あげた今回あげない
c = 0 #前回あげない今回あげた
for x in range(N):
  List[x][0] = min(a,c)
  List[x][1] = b
  a = List[x][0] + A[x]
  b = List[x][0] 
  c = List[x][1] + A[x]
List[x+1][0] = min(a,c)
List[x+1][1] = b

List2 = [[0 for _ in range(2)] for _ in range(N+1)]

before = True
a = 0 #前回あげた今回あげた
b = 0 #前回あげた今回あげない
c = 0 #前回あげない今回あげた
for x in range(N):
  List2[x][0] = min(a,c)
  List2[x][1] = b
  a = List2[x][0] + A[x]
  b = List2[x][0] 
  c = List2[x][1] + A[x]
  if x == 1:
    c = 2 * 10 ** 9 
List2[x+1][0] = min(a,c)
List2[x+1][1] = b
#print(List,List2)
print(min(List[N][0],List2[N][1]))

import bisect

Dict = {}
    
N = int(input())
A = list(map(int,input().split()))
Q = int(input())

count = 1
for a in A:
  if a in Dict:
    Dict[a].append(count)
  else:
    Dict[a] = [count]
  count += 1

for q in range(Q):
  L,R,Q = (map(int,input().split()))
  if not Q in Dict:
    print(0)
    continue
  LL = bisect.bisect_left(Dict[Q],L)
  RR = bisect.bisect_right(Dict[Q],R)
  print(RR-LL)
  
  
  

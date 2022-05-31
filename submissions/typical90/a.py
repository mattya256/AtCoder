def check(L,K,A,now):
  sum = 0
  KC = 0
  before = 0
  for x in A:
    x = x - before
    before = x + before
    sum += x
    if sum >= now:
      sum = 0
      KC += 1
  x = L - before
  sum += x
  if sum >= now:
    sum = 0
    KC += 1
  if KC >= K:
    return True
  else:
    return False
    

def nibun(min,max,L,K,A):
  if min >= max:
    xxx = min
    if check(L,K,A,min):
      return xxx
    else:
      return min-1
  now = int((min+max)/2)
  if check(L,K,A,now):
    return nibun(now+1,max,L,K,A)
  else:
    return nibun(min,now-1,L,K,A)


N,L = (map(int,input().split()))
K = int(input())
A = list(map(int,input().split()))
print(nibun(1,L,L,K+1,A))

  

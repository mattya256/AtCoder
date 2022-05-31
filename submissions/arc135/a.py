dict = {}

MOD = 998244353


def change(inta):
  sum = 0
  L = S = 0
  if inta>3:
    L = (inta + 1 ) // 2
    if not L in dict:
      LL = change(L)
      dict[L] = LL
    else:
      LL = dict[L]
    S = inta//2
    if not S in dict:
      SS = change(S)
      dict[S] = SS
    else:
      SS = dict[S]
    sum = LL * SS
  else:
    sum = inta
  return sum % MOD
    

X = int(input())
print(change(X)%MOD)
  

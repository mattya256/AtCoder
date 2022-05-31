S = input()
Dict = {}
count = sum = 0
for x in reversed(range(len(S))):
  #print(x,S[x],sum,count,Dict)
  if x >= len(S) - 2:
    pass
  else:
    if S[x] == S[x+1]:
      sum += count - Dict[S[x]]
      count = len(S) - x - 1
      Dict = {}
      Dict[S[x]] = count
  if not S[x] in Dict:
    Dict[S[x]] = 1
  else:
    Dict[S[x]] += 1
  count += 1
print(sum)

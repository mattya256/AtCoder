N= int(input())
S= input()

R = G = B = 0
for s in S:
  if s == 'R':
    R += 1
  if s == 'G':
    G += 1
  if s == 'B':
    B += 1
print(R%2 + G%2 + B%2)

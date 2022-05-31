AB = [int(x) for x in input().split(" ")]
A = AB[0]
B = AB[1]

B1 = B + 1
B2 = B - 1
if B1 % 10 ==A%10 or B2 % 10 == A%10:
  print("Yes")
else:
  print("No")

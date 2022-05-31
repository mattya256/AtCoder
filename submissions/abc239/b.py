from fractions import Fraction

X = int(input())
if X % 10 == 0:
  count = 0
else:
  count = 1
if X > 0:  
  print(int(Fraction(X)/Fraction(10)) )
else:
  print(int(Fraction(X)/Fraction(10)) - count)

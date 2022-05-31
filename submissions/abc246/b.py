import math

A,B = map(int,input().split())
L2 = A ** 2 + B ** 2
y2 = (B ** 2)/L2
x2 = (A ** 2)/L2
print(math.sqrt(x2),math.sqrt(y2))

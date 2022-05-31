import math
def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)

N,A,B = map(int,input().split())

sumN = (N * (N +1 ) )// 2

NA = N // A
sumNA = (A * NA * (NA+1))//2
NB = N // B
sumNB = (B * NB * (NB+1))//2

AB = lcm(A,B)
NAB = N //AB
sumNAB = (AB * NAB * (NAB+1))//2

print(sumN -sumNB - sumNA + sumNAB)

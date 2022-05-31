N = int(input())
A = list(map(int,input().split()))
MIN = 2 ** 30
def method(OR,XOR,bool,count):
  #print(count)
  OR = OR | A[count]
  if bool:
    XOR = XOR ^ OR
    OR = 0
  count += 1
  if count != N:
    return min(method(OR,XOR,True,count),method(OR,XOR,False,count))
  if count == N:
    XOR = XOR ^ OR
    return XOR
  
MIN = min(method(0,0,True,0),method(0,0,False,0))
print(MIN)
  

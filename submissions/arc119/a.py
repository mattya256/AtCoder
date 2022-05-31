N = int(input())

MIN = 10 ** 19
for b in range(61):
  bb = 2 ** b
  a = N // bb
  c = N % bb
  MIN = min(a + b + c,MIN)
  
print(MIN)

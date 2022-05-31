N,P,Q = map(int,input().split())
A = list(map(int,input().split()))
sum = 0
for a1 in range(N):
  for a2 in range(N):
    if a2 > a1:
      for a3 in range(N):
        if a3 > a2:
          for a4 in range(N):
            if a4 > a3:
              for a5 in range(N):
                if a5 > a4:
                  if (A[a1] * A[a2] %P* A[a3]%P * A[a4]%P * A[a5])%P == Q:
                    sum += 1
print(sum)

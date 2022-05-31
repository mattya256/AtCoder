x = input()
max = x
min = x
for i in range(len(x)):
  x = x[1:] + x[0]
  if x > max:
    max = x
  if x < min:
    min = x
print(min)
print(max)

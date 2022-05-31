a = input()
b = list(a)
x = ""
b.extend(b[0])
del b[0]
for c in b:
  x += c  
print(x)

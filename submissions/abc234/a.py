def fff(input = input):
  ret = input * input + 2 * input + 3
  return ret


x = int(input())
i = fff(fff(fff(x) + x) + fff(fff(x)))
print(i)

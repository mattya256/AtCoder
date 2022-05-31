Q = int(input())
List = []
i = 0
for x in range(Q):
  query = list(map(int,input().split()))
  #print(query)
  if query[0] == 1:
    #print(x,List)
    List.append([query[1],query[2]])
  else:
    c = query[1]
    sum = 0
    while(True):
      #print(x,i,List)
      if List[i][1] < c:
        sum += List[i][1]*List[i][0]
        c -= List[i][1]
        i += 1
      else:
        sum += c *List[i][0]
        List[i][1] = List[i][1] - c
        break
    print(sum)
       
    

s=input()

a={}

xxx=True

for x in s:

  if xxx:

    xxx =False

    ddd = x

  if x in a:

    a[x] +=1

  else:

    a[x] =1

l=ddd*a[ddd]

for key,value in a.items():

  if key==ddd:

    pass

  else:

    aa = True

    for count,x in enumerate(l):

      if x>key:

        l = l[:count]+key*value+l[count:]

        aa= False

        break

    if aa:

      l = l[:count+1]+key*value+l[count+1:]

print(l)

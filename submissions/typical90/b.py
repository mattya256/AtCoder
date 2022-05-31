def kakko(Migi,Hidari,w,max,Str):
  if w == "R":
    Migi += 1
    Str +="("
  else:
    Hidari += 1
    Str += ")"
  if Hidari>Migi or Migi > max/2:
    return
  if max == Migi+Hidari and Migi == Hidari:
    print(Str)
    return
  kakko(Migi,Hidari,"R",max,Str)
  kakko(Migi,Hidari,"L",max,Str)
  
N = int(input())
kakko(0,0,"R",N,"")
  

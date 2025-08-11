def Alpha_Hill_Pattern(n):

  for i in range(1,n+1,1):
    for j in range(n,i,-1):
      print(" ",end="")
    for k in range(97,97+i,1):
      print(chr(k),end="")
    for l in range(97+i-2, 97, -1):
      print(chr(l),end="")
    print()

Alpha_Hill_Pattern(4)

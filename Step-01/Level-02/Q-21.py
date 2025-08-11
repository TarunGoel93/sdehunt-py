def Hollow_Rectangle_Pattern(n):
  for i in range(0,n,1):
    for j in range(0,n,1):
      if (i==0 or i==n-1 or j==0 or j==n-1):
        print("*",end="")
      else:
        print(" ",end="")
    print()
Hollow_Rectangle_Pattern(4)
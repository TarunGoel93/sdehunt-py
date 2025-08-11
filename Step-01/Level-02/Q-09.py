def Diamond_Star_Pattern(n):

  for i in range(1,n+1,1):

    #print space first
    for j in range(n,i,-1):
      print(" ",end="")

    #print star
    for k in range(0,2*i-1,1):
      print("*",end="")

    print("")


  for i in range(1,n+1,1):

    for j in range(0,i-1,1):
      print(" ",end="")

    for k in range(0,(2*n-(2*i-1)),1):
      print("*",end="")

    print("")


Diamond_Star_Pattern(5)



def star_pattern(n):
  for i in range(n,0,-1):
    for j in range(1,i+1,1):
      print(j,end="")
    print("")

star_pattern(5)


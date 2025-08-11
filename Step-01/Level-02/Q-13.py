def Increasing_Number_Triangle_Pattern(n):
  x = 1
  for i in range(1,n+1,1):
    for j in range(1,i,1):
      print(x,end="")
      x+=1
    print()
Increasing_Number_Triangle_Pattern(5)
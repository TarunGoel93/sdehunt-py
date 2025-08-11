def Increasing_Letter_Triangle_Pattern(n):
  for i in range(1,n+1,1):
    for j in range(97,97+i,1):
      print(chr(j),end="")
    print()
Increasing_Letter_Triangle_Pattern(5)


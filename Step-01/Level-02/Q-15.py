def Reverse_Letter_Triangle_Pattern(n):
  for i in range(n,0,-1):
    for j in range(97,97+i,1):
      print(chr(j),end="")
    print()
Reverse_Letter_Triangle_Pattern(5)
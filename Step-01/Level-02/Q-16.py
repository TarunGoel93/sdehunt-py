def Alpha_Ramp_Pattern(n):
  for i in range(0,n,1):
    for j in range(0,i+1,1):
      print(chr(i+97),end="")
    print()
Alpha_Ramp_Pattern(5)
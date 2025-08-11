def The_Number_Pattern(n):
  size = 2*n-1
  for i in range(size):
    for j in range(size):
      min_d = min(i,j,size-i-1,size-j-1)
      value = n-min_d
      print(value,end="")
    print()
The_Number_Pattern(5)
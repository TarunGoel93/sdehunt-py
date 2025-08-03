n = 4

for i in range(1,n+1,1):
  #print start
  for j in range(1,i+1,1):
    print(j,end="")

  #print space
  for k in range(0,(2*(n-i)),1):
    print("*",end="")

  #print star
  for l in range(1,i+1,1):
    print(l,end="")

  print("")



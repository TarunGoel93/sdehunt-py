n = 4

for i in range(1,n+1,1):

  #print space first
  for j in range(n,i,-1):
    print(" ",end="")

  #print star
  for k in range(0,2*i-1,1):
    print("*",end="")

  print("")
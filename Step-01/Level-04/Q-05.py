a = 60
b = 36
max = 0
count = 0
for i in range(1,a+1,1):
  for j in range(1,b+1,1):
    if(a%i==0 and b%j==0):
      if(i==j):
        count+=1
        if(i>max):
          max=i

if count == 1:
  print(max)
else:
  print(max)

       
  

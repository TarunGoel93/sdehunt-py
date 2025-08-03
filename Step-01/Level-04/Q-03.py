x = 10
temp = x

rev = 0
if(x<0):
  x = abs(x)

while(x!=0):
  digit = x%10
  rev = rev*10+digit
  x = x//10

if(rev==temp):
  print(f"{True}+{rev}")
else:
  print(f"{False}+{rev}")


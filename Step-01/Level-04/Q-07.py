class Solution:
  def isPrime(self,n):
    count = 0
    for i in range(2,n,1):
      if(n%i==0):
        count+=1

    if(count<=1):
      return False
    else:
      return True

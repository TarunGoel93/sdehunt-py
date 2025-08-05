import math
class Solution:
  def isPrime(self,n):
    r = []
    for i in range(1,int(math.sqrt(n))+1,1):
      if n%i==0:
        r.append(i)
        if i!=n//i:
          r.append(n//i)

    if len(r)==2:
      return True
    else:
      return False
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.isPrime(7))
      
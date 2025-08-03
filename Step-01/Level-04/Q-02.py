class Solution:
  def reverseDigits(self,n):
    temp = n
    if n<0:
      n = abs(n)
    rev = 0
    while(n!=0):
      digit = n%10
      rev = rev*10+digit
      n = n//10

    if(temp<0):
      return -rev
    else:
      return rev
    
if __name__ == "__main__":
  obj = Solution()
  print(obj.reverseDigits(-67))
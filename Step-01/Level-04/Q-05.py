class Solution:
    def isArmstrong(self, n):
      original = n
      count = 0
      while(n!=0):
         digit = n%10
         count+=1
         n = n//10

      new_orginal = original
      sum = 0
      while(original!=0):
         digit = original%10
         sum += digit**count
         original = original//10

      if new_orginal==sum:
         return True
      return False

         
if __name__ == "__main__":
    obj = Solution()
    print(obj.isArmstrong(1000))

'''
Company Tags
VMWare Oracle
'''
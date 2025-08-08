class Solution:
    def largest(self, arr):
        max = arr[0]
        for i in range(0,len(arr),1):
           if(max<arr[i]):
              max = arr[i]
        return max
             
if __name__== "__main__":
  obj = Solution()
  print(obj.largest([10,10,10,10]))

'''
 Company Tags
 Infosys Oracle Wipro MorganStanley 
'''
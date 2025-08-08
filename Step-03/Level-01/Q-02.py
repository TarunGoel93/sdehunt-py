class Solution:
    def getSecondLargest(self, arr):
        first_largest = arr[0]
        sec_largest = -1
        for i in range(0,len(arr),1):
            if first_largest<arr[i]:
                sec_largest = first_largest
                first_largest = arr[i]
            elif arr[i] != first_largest and arr[i] > sec_largest:
                sec_largest = arr[i]
        return sec_largest
    
if __name__== "__main__":
  obj = Solution()
  print(obj.getSecondLargest([10, 10, 10]))

'''
Company Tags
SAP Labs  Rockstand'
'''
       
       
class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(0,len(arr)-1,1):
            if(arr[i]>arr[i+1]):
                return False
        return True
if __name__== "__main__":
  obj = Solution()
  print(obj.isSorted([1, 2, 3, 4, 5,-1]))
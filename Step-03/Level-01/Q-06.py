class Solution:
    def linearSearch(self, nums, target):
        for i in range(0,len(nums),1):
            if nums[i]==target:
                return i
        return -1
if __name__== "__main__":
  obj = Solution()
  print(obj.linearSearch([1,2,3,4,5,6,7],5))
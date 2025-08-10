class Solution:
    def rotateArrayByOne(self, nums):
        temp = nums[0]
        for i in range(1,len(nums),1):
            nums[i-1] = nums[i]
        nums[-1] = temp
        return nums
if __name__== "__main__":
  obj = Solution()
  print(obj.rotateArrayByOne([-1, 0, 3, 6]))

'''
Company Tags
Amazon Microsoft MAQSoftware
'''
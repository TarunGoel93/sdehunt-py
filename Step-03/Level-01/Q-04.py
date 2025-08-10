class Solution:
    def removeDuplicates(self, arr):
        r = []
        for i in range(0,len(arr)-1,1):
            if(arr[i]!=arr[i+1]):
                r.append(arr[i])
        r.append(arr[-1])
        return r
if __name__== "__main__":
  obj = Solution()
  print(obj.removeDuplicates([-2, 2, 4, 4, 4, 4, 5, 5]))

'''
Company Tags
Zoho MorganStanley Microsoft Samsung Google Wipro Xome
'''               
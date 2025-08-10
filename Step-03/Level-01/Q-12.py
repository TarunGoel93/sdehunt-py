class Solution:
    def findUnique(self, arr):
        count_map = {}
        for i in arr:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i]=1
        for key,value in count_map.items():
            if value ==1:
                return key
        return -1
            
if __name__== "__main__":
  obj = Solution()
  print(obj.findUnique([1]))

'''
Company Tags
Amazon
'''
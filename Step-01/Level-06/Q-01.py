class Solution:
    def countFreq(self, arr):
        count_map = {}
        for i in arr:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i]=1
        
        result = [[key,value] for key,value in count_map.items()]
        return result
    
if __name__== "__main__":
  obj = Solution()
  print(obj.countFreq([1,2,3,1,2]))


            
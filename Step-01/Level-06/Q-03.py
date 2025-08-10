class Solution:
    def mostFreqEle(self, arr):
        count_map = {}
        for i in arr:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i]=1
        max = 0
        r = -1
        for key,value in count_map.items():
            if value>max or (value == max and key > r):
                max = value
                r = key
        return r
if __name__== "__main__":
  obj = Solution()
  print(obj.mostFreqEle([0,5,3,1]))


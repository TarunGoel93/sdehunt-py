class Solution:
    def findUnion(self, a, b):
        r = []
        f_r = []
        for i in range(0,len(a),1):
            r.append(a[i])
        for j in range(0,len(b),1):
            r.append(b[j])
        r.sort()
        for k in range(0,len(r)-1,1):
            if(r[k]!=r[k+1]):
                f_r.append(r[k])
        f_r.append(r[-1])
        return f_r
if __name__== "__main__":
  obj = Solution()
  print(obj.findUnion([1, 1, 1, 1, 1],[2, 2, 2, 2, 2]))

'''
Company Tags
Amazon
'''
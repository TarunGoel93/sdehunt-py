class Solution: 
    def selectionSort(self, arr):
        for i in range(0,len(arr)-1,1):
            mini = i
            for j in range(i,len(arr),1):
                if(arr[j]<arr[mini]):
                    mini = j
            temp = arr[mini]
            arr[mini] = arr[i]
            arr[i] = temp
        return arr
if __name__== "__main__":
  obj = Solution()
  print(obj.selectionSort([5,4,3,2,1,6]))

'''
Company Tags
Microsoft Medlife
'''
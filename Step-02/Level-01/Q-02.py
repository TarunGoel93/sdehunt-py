class Solution:
    def bubbleSort(self,arr):
        for i in range(0,len(arr),1):
            for j in range(0,len(arr)-1,1):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr
if __name__== "__main__":
  obj = Solution()
  print(obj.bubbleSort([5,4,3,2,1,6]))

'''
Company Tags
Microsoft Wipro SAPLabs Cisco Nagarro redBus Accenture Huawei
'''
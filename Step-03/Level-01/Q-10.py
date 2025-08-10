class Solution:
    def missingNum(self, arr):
        n = len(arr)
        sum1 = 0
        for i in range(n+1,0,-1):
           sum1+=i
        

        sum2 = 0
        for i in range(0,len(arr),1):
           sum2+=arr[i]


        return sum1-sum2
        
    

if __name__== "__main__":
  obj = Solution()
  print(obj.missingNum([1]))


'''
Company Tags
Flipkart  MorganStanley Accolite Amazon Microsoft D-E-Shaw OlaCabs Payu Visa Intuit Adobe Cisco Qualcomm TCS
'''
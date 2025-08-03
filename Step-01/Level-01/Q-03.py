class Solution:
  def studentGrade(self, marks):
    if(marks>=90 and marks<=100):
      return "Grade A" 
    elif(marks>=70 and marks<90):
      return "Grade B"
    elif(marks>=50 and marks<70):
      return "Grade C"
    elif(marks>=35 and marks<50):
      return "Grade D"
    else:
      return "Fail"
    
if __name__== "__main__":
  obj = Solution()
  print(obj.studentGrade(95))
  print(obj.studentGrade(14))
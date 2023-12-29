class Solution:
    def largestNumber(self, nums: List[int]) -> str:
         def isgreater(s1,s2):
            n1=str(s1)
            n2=str(s2)
            return int(n2+n1) > int(n1+n2)
         for i in range (len(nums)):
             for j in range (len(nums)-i-1):
                 if isgreater(nums[j],nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
         nums=list(map(str,nums))
         return str(int("".join(nums)))
       
        
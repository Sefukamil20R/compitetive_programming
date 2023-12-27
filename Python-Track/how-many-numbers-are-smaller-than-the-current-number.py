class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         
         ans=[]
         for i in range (len(nums)):
             count=0
             for j in range (len(nums)):
                 if nums[j] < nums[i]:
                     count+=1
             ans.append(count)
         return ans 


            # result=[0]*101
            # for num in nums:
            #     result[num]+=1

            

        
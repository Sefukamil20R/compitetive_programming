class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        end = nums[-1]
        res , n = 0 , len(nums)
        for i in range(n-2,-1 , -1):
            if end < nums[i]:
                 div = ceil(nums[i]/end)
                 end = nums[i]//div
                 res += div - 1
            else:
                end = nums[i]
           
        return res 
        
                


        
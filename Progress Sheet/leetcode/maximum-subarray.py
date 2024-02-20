class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum =nums[0]
        maxx = nums[0]
        for i in range( 1, len(nums)):
            
            
            if cursum < 0:
                cursum = 0
            cursum += nums[i]
            maxx = max(cursum , maxx)   
        return maxx 

        
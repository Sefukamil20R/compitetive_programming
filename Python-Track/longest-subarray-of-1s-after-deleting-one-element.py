class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , r =  0, 0
        maxx  = 0
        no_zero = 0
        while r < len(nums):
            if nums[r] == 0:
                no_zero += 1
            while no_zero > 1:
                if nums[l] == 0:
                    no_zero -= 1
                l += 1
            maxx = max (maxx, r - l)
            r += 1    
            
            
        return maxx 
            



                                                                                                                                                          
        
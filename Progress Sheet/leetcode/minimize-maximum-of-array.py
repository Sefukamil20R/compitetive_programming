class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx , count  = 0 , 0
        prefix = 0 
        for i in range(len(nums)):
            prefix += nums[i]
            count += 1
            avg = ceil(prefix/count)
            maxx = max(avg , maxx)
        return maxx

        
        
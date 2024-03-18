class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
       
        nums.sort()
        r =  len(nums) - 1
        count = 0
        mod = 10**9 + 7
        for i, left in enumerate(nums):
            while i<=r and left + nums[r]>target:
                r-=1
            if i<=r:
                count+=2**(r-i)
        return count%mod
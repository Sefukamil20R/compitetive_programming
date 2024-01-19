class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
           prefix[i] =prefix[i-1] + nums[i]
        suffix[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
           suffix[i] = suffix[i+1] + nums[i]
        ans = []
        for i in range(len(nums)):
            ls = i * nums[i] - prefix[i]
            rs = suffix[i] - (len(nums) - i - 1) * nums[i]
            ans.append(ls + rs)
        return ans

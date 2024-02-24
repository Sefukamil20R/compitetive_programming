class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                val = stack.pop()
                res[val[1]] = nums[i]
            
            stack.append((nums[i],i))
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                val = stack.pop()
                res[val[1]] = nums[i]
        return res
            
         

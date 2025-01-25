class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            prefix.append(current_sum)
        return prefix
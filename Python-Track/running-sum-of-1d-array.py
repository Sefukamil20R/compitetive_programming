class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix.append(summ)
        return prefix

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        valid_Selection = 0 
        for i in range(len(nums)):
            right = total - left
            if nums[i] == 0 and left == right:
                valid_Selection += 2
            elif nums[i] == 0 and left == right - 1:
                valid_Selection += 1
            elif nums[i] == 0 and left - 1 == right:
                valid_Selection += 1

            left += nums[i]
        return valid_Selection 



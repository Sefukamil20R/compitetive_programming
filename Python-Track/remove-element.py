class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        count = 0 
        for r in range(len(nums)):
           if nums[r] != val:
               nums[r],nums[l] = nums[l], nums[r]
               l+=1
               count += 1
        return count
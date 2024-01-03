class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
           count = 1
           store = 1
           for i in range(1,len(nums)):
               if nums[i] != nums[i-1]:
                   nums[store] = nums[i]
                   store += 1
                   count += 1
           return count 

        

        
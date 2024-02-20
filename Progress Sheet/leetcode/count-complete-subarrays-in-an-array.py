class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nos = set(nums)
        counter = defaultdict(int)
        count = 0
        l = 0
        for i in range(len(nums)):
            counter[nums[i]] += 1
            while  len(counter) == len(nos):
               count += len(nums) - i
               counter[nums[l]] -= 1
               if counter[nums[l]] == 0:
                   del counter[nums[l]]
               l += 1
               
            
        return count

        
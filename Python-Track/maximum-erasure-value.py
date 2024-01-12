class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0 
        
        seen = set()
        maxx = 0
        total  = 0
        for r in range(len(nums)):
            if nums[r] not in seen:
                  total += nums[r]
                  seen.add(nums[r])
            else:
                while nums[l] != nums[r]:
                    seen.remove(nums[l])
                    total -= nums[l]
                    l += 1
                    
                l += 1
            maxx = max (maxx , total)

        return maxx
            

        
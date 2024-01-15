class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = res = count = oddC = 0
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                oddC += 1
                count = 0 
                while oddC == k:
                    if nums[l]%2 == 1:
                        oddC -= 1
                    l += 1
                    count += 1
            res += count 
        return res
                
                    
        
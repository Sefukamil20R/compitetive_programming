class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for ind , val in enumerate (nums):
            if ind > 0 and val == nums[ind-1]:
                   continue
            if val > 0:
                break
            l , r = ind+1 , len(nums)-1
            while l < r:
                threesum = nums[l] + nums[r] + val 
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    ans.append([val , nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        return ans 
        
                
            
            
            

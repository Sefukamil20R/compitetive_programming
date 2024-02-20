class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]
        for i in range(1,len(nums)):
            if maxx < i :
                return False
            # if maxx < nums[i] :
            #     maxx = nums[i] + i
            maxx = max(maxx , nums[i] + i)
            
        return True
        
        
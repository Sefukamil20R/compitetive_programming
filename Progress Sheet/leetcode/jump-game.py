class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maxx = nums[0]
        # for i in range(1,len(nums)):
        #     if maxx < i :
        #         return False
        #     # if maxx < nums[i] :
        #     #     maxx = nums[i] + i
        #     maxx = max(maxx , nums[i] + i)
            
        # return True
        n = len(nums)
        goal = n-1 
        count = 0
        for i in range(n - 2,-1,-1):
            if nums[i] + i >= goal:
                goal = i
                count += 1
        
        return goal  == 0



        
        
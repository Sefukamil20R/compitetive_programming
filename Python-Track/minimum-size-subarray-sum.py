class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total,l = 0,0
        ans = len(nums)+1
        for r in range (len(nums)):
            total += nums[r]
            while total >= target:
                ans = min (ans, r-l+1)
                total -= nums[l]
                l += 1
        return 0 if ans ==len(nums)+1 else ans

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # total=0
        # left=0
        # right=0
        # res=float("inf")
        # while right <len(nums):
        #      total+=nums[right]
        #      while total>=target:
        #         res=min(res,right-left+1)
        #         total-=nums[left]
        #         left+=1
        #      right+=1
        # return 0 if res==float("inf") else res   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
     
     
     
     
        # total = 0
        # l = 0
        # j = len(nums)+1
        # for r in range(len(nums)):
        #     total += nums[r]
        #     while total >= target:
        #         if (r-l+1) < j:
        #             j = r-l+1
        #         total -= nums[l]
        #         l = l+1
        # return 0 if j == len(nums)+1 else j  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # total=0
        # left=0
        # right=0
        # res=float("inf")
        # while right <len(nums):
        #      total+=nums[right]
        #      while total>=target:
        #         res=min(res,right-left+1)
        #         total-=nums[left]
        #         left+=1
        #      right+=1
        # return 0 if res==float("inf") else res   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
     
     
     
     
        # total = 0
        # l = 0
        # j = len(nums)+1
        # for r in range(len(nums)):
        #     total += nums[r]
        #     while total >= target:
        #         if (r-l+1) < j:
        #             j = r-l+1
        #         total -= nums[l]
        #         l = l+1
        # return 0 if j == len(nums)+1 else j
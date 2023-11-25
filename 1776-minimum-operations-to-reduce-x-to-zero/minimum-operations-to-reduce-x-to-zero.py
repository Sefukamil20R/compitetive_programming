class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
            target=sum(nums)-x
            cursum=0
            max_window=-1
            left=0
            for right in range(len(nums)):
                    cursum+=nums[right] 
                    while  left <=right and cursum > target:
                            cursum-=nums[left]  
                            left+=1
                    if cursum==target:
                            max_window=max(max_window,right-left+1)
            return  -1 if max_window==-1 else len(nums)- max_window
          
        
       
        
       

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort() 
        for i in range(len(nums)-1,1,-1):
            r = i - 1
            l = 0
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += ( r - l)
                    r -= 1
                else:
                    l += 1
                    
                
        return count 
        

        
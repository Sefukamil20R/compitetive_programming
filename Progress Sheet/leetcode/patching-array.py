class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cover,patches,i   = 0 , 0 , 0
    
       
        while cover < n:
            if i < len(nums) and  nums[i] <= cover + 1 :
                cover += nums[i]
                i += 1
            else:
                patches += 1
                cover += cover + 1
        return patches
        
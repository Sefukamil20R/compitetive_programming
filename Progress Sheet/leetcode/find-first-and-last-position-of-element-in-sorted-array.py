class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left , right = -1 , len(nums)-1
        ans = []
        if not nums:
            return [-1,-1]
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            ans.append(right)
        else:
            return [-1,-1]
        left , right = 0 , len(nums) 
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        ans.append(left)
        return ans


        
        
        
            
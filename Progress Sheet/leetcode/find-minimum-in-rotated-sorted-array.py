class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = -1 , len(nums)-1
        while left + 1 < right:
            mid =  (left + right)//2
            if nums[mid] > nums[right]:
                 left = mid
            else:
                right = mid
        return nums[right] 

        
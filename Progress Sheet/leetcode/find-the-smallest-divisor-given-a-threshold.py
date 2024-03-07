class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        def helper (tre):
            summ = 0
            for i in range(len(nums)):
                summ += ceil (nums[i]/tre)
            return summ

        left , right = 0 , max(nums)   

        while left + 1 < right:
            mid = (left + right )//2
            val = helper(mid)
            if val <= threshold:
                right =  mid
            else:
                left = mid
        return right


        
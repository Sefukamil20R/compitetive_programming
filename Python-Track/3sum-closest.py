class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float ("inf")
        for i in range(len(nums)-2):
             l , r = i + 1, len(nums)-1
             while l < r:
                curS = nums[l] + nums[r] + nums[i]
                if abs (curS - target) < abs (ans - target):
                    ans = curS
                if curS < target:
                    l += 1
                else :
                    r -= 1
             
        return ans 
                

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []
        n = len(nums)
        def back(start):
            ans.append(sub[:])
            for i in range(start, n):
                    sub.append(nums[i])
                    back(i+1)
                    sub.pop()
        back(0)
        return ans

                
        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []
        seen = set()
        n = len(nums)
        def back(start):
            val = tuple(sorted(sub[:]))
            if val not in seen:
                seen.add(val)
                ans.append(sub[:])
            for i in range(start, n):
                    sub.append(nums[i])
                    back(i+1)
                    sub.pop()
        back(0)
        return ans
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def permutations(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
        
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    path.append(nums[i])
                    permutations(path)
                    path.pop()
                    seen.remove(nums[i])
        permutations([])  
        return ans


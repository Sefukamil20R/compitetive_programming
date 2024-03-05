class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        summ = 0
        seen = set()
        def back(path):
            nonlocal summ
            if summ > target:
                return
            if summ == target:
                val = tuple(sorted(path[:]))
                if val not in seen:
                    seen.add(val)
                    ans.append(path[:])

            for i in range(len(candidates)):
                summ += candidates[i]
                path.append(candidates[i])
                back(path)
                summ -= candidates[i]
                path.pop()

        back([])
        return ans
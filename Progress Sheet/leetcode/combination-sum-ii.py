class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        summ = 0
        candidates.sort()
        seen = set()
        def back(start ,path):
            nonlocal summ
            if summ > target:
                return
            if summ == target:
                val = tuple(sorted(path[:]))
                if val not in seen:
                    seen.add(val)
                    ans.append(path[:])
            x = 0
            for i in range(start , len(candidates)):
                if candidates[i] != x:
                    summ += candidates[i]
                    path.append(candidates[i])
                    back(i+1 , path)
                    summ -= candidates[i]
                    x = path.pop()

        back(0,[])
        return ans
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        seen = set()
        visit = set()
        def back(start , path):
            
            if len(path) == k:
              val = tuple(sorted(path[:]))
              if val not in seen:
                if sum(path) == n:
                    ans.append(path[:])
                    seen.add(val)
                    return
                else:
                    return
            
            for i in range(start,10):
                path.append(i)
                back(i + 1, path)
                path.pop()
        back(1,[])
        return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(fir,path):
            if len(path) == k :
                ans.append(path[:])
                return
            for num in range(fir , n + 1):
                path.append(num)
                back(num + 1, path)
                path.pop()
        back(1,[])
        return ans

        
         
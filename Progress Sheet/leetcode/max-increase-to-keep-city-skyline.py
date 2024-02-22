class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        coulumns = list(zip(*grid))
        ans = 0 
        print(coulumns)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans += min(max(grid[i]),max(coulumns[j]))-grid[i][j]
        return ans 



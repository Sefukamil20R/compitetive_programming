class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
         costs.sort(key = lambda x : x[0] - x[1] )
         n = len(costs)
         asum = 0
         bsum = 0
         for i in range(n//2):
             asum += costs[i][0]
         for i in range(n//2  ,n):
             asum += costs[i][1]
         return asum + bsum
             
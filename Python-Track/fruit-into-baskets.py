class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 
        maxx = 0
        treefruit = defaultdict(int)
        for r in range (len(fruits)):
            treefruit[fruits[r]] += 1
            while len(treefruit) > 2 :
                treefruit[fruits[l]] -= 1
                if treefruit[fruits[l]] == 0:
                    del treefruit[fruits[l]]
                l += 1
            maxx = max(maxx , r -l +1 )
        return maxx

        
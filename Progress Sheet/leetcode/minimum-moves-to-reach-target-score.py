class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while maxDoubles > 0 and target > 1:
            res += target %2
            res += 1  
            maxDoubles -=1  
            target //= 2
        return res + target -1
        


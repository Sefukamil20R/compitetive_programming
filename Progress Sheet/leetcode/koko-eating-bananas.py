class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            count = 0
            for i in range(len(piles)):
              count += ceil(piles[i]/k)
            
            return count 
        left , right =0 , max(piles)
        while left + 1 < right:
            mid = (left + right)//2 
            val = helper(mid)
            if  val <= h:
                right = mid
            else:
                left =  mid
        return right
             


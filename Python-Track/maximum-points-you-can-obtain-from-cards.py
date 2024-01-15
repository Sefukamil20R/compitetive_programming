class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
         win = sum(cardPoints[:k])
         maxx = win
         l = k - 1 
         r = 0 
         while l >= 0:
             win -= cardPoints[l]
             r -= 1
             win += cardPoints[r]
             l -= 1
             
            
             maxx = max (maxx , win )
         return maxx

        
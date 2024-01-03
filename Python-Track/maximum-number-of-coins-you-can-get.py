class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        k = n//3 
        piles.sort()
        print(piles)
        summ = 0
        for i in range (k, n-1, 2):
            summ += piles[i]
        return summ


        

        
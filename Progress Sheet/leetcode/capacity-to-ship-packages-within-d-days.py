class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(cap):
            summ = 0
            count = 0
            for i in range(len(weights)):
                
                summ += weights[i]
                if summ == cap:
                    count += 1
                    summ = 0
                elif summ > cap:
                    count += 1
                    summ = weights[i]
            if summ > 0 :
                count += 1
            
            return count
        left , right =  max(weights) - 1 , sum(weights)
        while left + 1 < right:
              mid = (left + right)//2
              val = helper(mid)
              if val <= days:
                  right = mid
              else:
                  left = mid
        return right

                
        
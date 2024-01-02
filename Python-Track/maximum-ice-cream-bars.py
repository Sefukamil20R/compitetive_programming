class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
          maxx = max (costs)
          total = 0
          
          counting = [0]*(maxx+1)
          for num in costs:
              counting[num]+=1
          sorted_A = []
          for i in range (maxx+1):
              sorted_A.extend([i]*counting[i])
          count = 0
          for i in range(len(sorted_A)):
              total += sorted_A[i]
              if total <= coins:
                  count += 1
              else:
                  break
          return count




        
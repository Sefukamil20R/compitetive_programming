class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def helper(rad):
            p1 , p2  = 0 , 0 
            while p1 < len(houses) and p2 < len(heaters):
                    if abs(houses[p1] -  heaters[p2]) <= rad:
                        p1 += 1
                    else:
                        p2 += 1
            if houses[p1:]: 
                return False
            else:
                return True 
        left , right = -1 , 10**9
        while left + 1 < right:
                mid = (left + right)//2
                val = helper(mid)
                if val:
                    right = mid
                else:
                    left = mid
        return right
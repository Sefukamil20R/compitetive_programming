class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxdes =  max(trips , key = lambda x : x[2])
        prefix = [0]*(maxdes[2]+1)
        for num , pick , drop in trips:
            prefix[pick] += num
            prefix[drop] -= num
        total = 0
        for i in range(len(prefix)):
            total += prefix[i]
            if total > capacity :
                return False
        return True





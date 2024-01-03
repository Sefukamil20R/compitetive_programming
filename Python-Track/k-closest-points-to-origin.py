class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Distance = defaultdict(list)
        for i,j in points:
            dis = sqrt(i**2 + j**2)
            Distance[dis].append([i,j])
        sort = list(Distance.keys())
        sort.sort()
        ans = []
        
        for i in range(k):
            ans.extend(Distance[sort[i]])
            if len(ans)==k:
                break
        return ans
       
       
           
        
      

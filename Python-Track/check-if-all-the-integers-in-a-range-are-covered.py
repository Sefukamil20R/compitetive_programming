class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
            res=set()
            for i in range(left,right+1):
                    for rain in ranges:
                        new_set={ j for j in range(rain[0],rain[1]+1)}
                        if i in new_set:
                            res.add(i)
                            break
                   
            return len(res)==(right-left+1)
        
                
                
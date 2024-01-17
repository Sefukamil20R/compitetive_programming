class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f , s = 0 , 0
        res = []
        while f < len(firstList) and s < len(secondList):
           x = max(firstList[f][0],secondList[s][0])
           y = min(firstList[f][1] ,secondList[s][1])
           if x <= y:
               res.append([x,y])
           if firstList[f][1] < secondList[s][1]:
                    f += 1
           else:
                 s += 1
        return res


        
        
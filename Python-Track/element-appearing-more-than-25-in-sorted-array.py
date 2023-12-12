class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
           diss=Counter(arr)
           print(diss)
           lenn=len(arr)//4
           for key,value in diss.items():
                if value > lenn:
                    return key
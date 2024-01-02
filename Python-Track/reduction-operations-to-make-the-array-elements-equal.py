class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
       
        count = Counter(nums)
        sett = list(set(nums))
        sett.sort()
        i = 0
        oper = 0
        i , j = 0 , len(sett)-1
        while j >= 0 :
            oper += (j - i)*count[sett[j]]
            j-=1
        return oper
        


        
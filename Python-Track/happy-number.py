class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
             summ=0
             for s in str(n):
                summ+=pow(int(s),2)
             if summ in seen :
                return False
             seen.add(summ)
             n=summ
        return True
        
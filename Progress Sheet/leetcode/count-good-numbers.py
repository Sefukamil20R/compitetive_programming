class Solution:
    def __init__(self):
        self.used = {}
    def countGoodNumbers(self, n: int) -> int:
        
        if n == 1:
            return 5
        if n == 2:
            return 20
        if n not in self.used:
            a = n// 2
            if n % 2 != 0:
                self.used[n] = ( self.countGoodNumbers(a) * self.countGoodNumbers((a + 1)))%((10**9) + 7)
            else:
                self.used[n]  = (self.countGoodNumbers((n-1))*4)% ((10**9) + 7)
            return self.used[n]%(10**9 + 7)
        else:
            return self.used[n]%(10**9 + 7)
            
           
        
        
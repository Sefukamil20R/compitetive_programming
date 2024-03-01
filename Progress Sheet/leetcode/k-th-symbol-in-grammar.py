class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k % 2 != 0 :
            return self.kthGrammar(n,ceil(k/2))
        elif k %2 == 0:
            val = self.kthGrammar(n,ceil(k/2))
            if val == 0:
                return 1
            else:
                return 0
        
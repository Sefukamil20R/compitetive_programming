class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        Tcount = 0
        Fcount = 0
        l = 0
        maxx = 0 
        for r in range (len(answerKey)):
            if answerKey[r] == "T":
                Tcount += 1
            else:
                Fcount += 1
        
            while min(Tcount,Fcount) > k:
                if answerKey[l] == "T":
                    Tcount -= 1
                else:
                        Fcount -= 1
                l += 1
            maxx = max (maxx , r-l+1)
        return maxx



                




        
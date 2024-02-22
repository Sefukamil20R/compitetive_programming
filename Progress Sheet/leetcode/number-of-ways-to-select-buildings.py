class Solution:
    def numberOfWays(self, s: str) -> int:
        onecount , zerocount = 0 , 0
        pre1 = [0]* (len(s)+1)
        pre0 = [0]* (len(s)+1)
        res = 0
        for i in range (len(s)) :
            if s[i] == "0":
                zerocount += 1
                pre1[i + 1] = onecount
            else:
                onecount += 1
                pre0[i +1] = zerocount
            pre1[i +1] += pre1[i]
            pre0[i +1] += pre0[i]
       
        for i in range(len(s)):
            if s[i] == "0":
                res += pre0[i]
            else:
                res += pre1[i]
        return res



        
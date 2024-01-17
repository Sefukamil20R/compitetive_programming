class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
         prefix = [0]*len(s)
         total = 0
         res = []
         for i in range(len(shifts)):
             if shifts[i][2] == 0:
                 prefix[shifts[i][0]] -= 1
                 if shifts[i][1] < len(s)-1:
                      prefix[shifts[i][1]+1] += 1
             else:
                 prefix[shifts[i][0]] += 1
                 if shifts[i][1] < len(s)-1:
                      prefix[shifts[i][1]+1] -= 1
         for i in range(len(prefix)):
             total += prefix[i]
             res.append(total)
         lists = list(s)
         for i in range(len(lists)):
             lists[i] = chr(((ord(lists[i])+res[i]-96)%26  or 26 )+ 96)
         return "".join(lists)

         


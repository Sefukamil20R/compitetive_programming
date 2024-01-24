class Solution:
    def maxScore(self, s: str) -> int:
        total = 0
        prefix = []
        count = 0
        maxx = 0
        for i in range(len(s)):
            total += int(s[i])
            prefix.append(total)
        a = prefix[-1]
        print(prefix)
        for i in range(len(prefix)-1):
            if s[i] == "0":
                count += 1 
            else:
                a -=  1
            
            
            maxx = max(maxx , count + a)
        
        return maxx
            
            
    

           
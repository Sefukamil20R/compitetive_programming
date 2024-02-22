class Solution:
    def balancedString(self, s: str) -> int:
        res = len(s)  
        count = Counter(s) 
        print(count)
        l = 0  
        for i, c in enumerate(s):
           count[c] -= 1  
           while l < len(s) and all(count[c] <= len(s) // 4 for c in 'QWER'):
                  res = min(res, i - l + 1)  
                  count[s[l]] += 1 
                  l += 1  
    
        return res  
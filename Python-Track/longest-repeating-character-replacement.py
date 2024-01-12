class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0 
        maxx = 0
        for r in range (len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1 
            maxx = max (maxx , (r - l + 1))
        return maxx
            
                



     
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVow , l , r, count = 0,0,0,0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for r in range (len(s)):
            if s[r] in vowels:
                 count += 1
            if (r-l+1) > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            maxVow = max (maxVow , count)
        return maxVow
            
                
            





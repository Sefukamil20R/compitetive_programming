class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0
        seen = set()
        maxW = 0
        while r < len(s):
            if s[r] in seen :
                maxW = max (maxW,r-l)
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                l += 1
            else:
                seen.add(s[r])
            r += 1
        maxW = maxW = max (maxW,r-l)
        return maxW

            
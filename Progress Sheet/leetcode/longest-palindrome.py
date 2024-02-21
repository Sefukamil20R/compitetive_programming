class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res =  len(s)
        odds = 0
        for i in count:
           if count[i] %2 == 1:
               odds += 1
        print(odds)
        if odds > 1:
             res -= odds -1
        return res
        
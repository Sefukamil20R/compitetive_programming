# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start , end = 0 , n-1
        while start <= end:
            bad = (start + end) //2
            if not isBadVersion(bad):
                 start = bad + 1
            else:
                end = bad - 1
        return start 
        

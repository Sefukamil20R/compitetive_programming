class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = 0
        left ,right = 0,0
        for i in range(1,n+1):
            tot += i
        for i in range(1,n+1):
            left += i
            right = (tot-left+i)
            if left == right:
                return i
        return -1


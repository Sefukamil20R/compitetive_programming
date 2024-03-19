class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        cand = []
        ans = []
        for i in range(len(s)):
            if s[i] == "|":
                cand.append(i)
        print(cand)
        for l , r in queries:
            if s[l] == "|":
                left = bisect_left(cand,l)
            else:
                left = bisect_right(cand,l)
            right = bisect_left(cand,r)
            if s[r]!= "|":
                right -= 1 
            if left >= right:
                ans.append(0)
                continue
            ans.append((cand[right]-cand[left]+1)-(right - left + 1))
        return ans
           
        
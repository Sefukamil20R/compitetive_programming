class Solution:
    def partitionLabels(self, s: str) -> List[int]: 
        cur = 0
        res = []
        lastOccur = {}
        for i in range(len(s)):  
             lastOccur[s[i]] = i
        while cur < len(s):
            end =   lastOccur[s[cur]]  #8
            j = cur + 1#1
            while j < end:
                end = max(end ,lastOccur[s[j]])
                j += 1
            res.append(end -cur + 1)
            cur = end + 1
        return res

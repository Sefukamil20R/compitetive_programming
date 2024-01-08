class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        ind = k - 1
        s1Count = Counter (s1)
        s2Count = Counter(s2[:ind])
        while ind < len(s2):
            s2Count[s2[ind]] += 1
            if s2Count == s1Count:
                return True 
            s2Count[s2[ind-k+1]] -= 1
            if s2Count[s2[ind-k+1]] == 0:
                del s2Count[s2[ind-k+1]]
            ind += 1
        return False
              
                  
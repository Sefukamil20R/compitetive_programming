class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       strs.sort(key=lambda x : len(x))
       answer=""
       for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                   return answer
            else:
                answer+=strs[0][i]
            
       return answer


                    
        
                    
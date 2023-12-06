class Solution:
    def printVertically(self, s: str) -> List[str]:
            ans=[]
            lists=s.split()
            maxx=0
            for s in lists:
                maxx=max(maxx,len(s))
            for i in range(maxx):
                strs=""
                for j in range(len(lists)):
                    if i < len(lists[j]):
                        strs+=lists[j][i]
                    else:
                        strs+=" "
                ans.append(strs.rstrip())
            return ans
                
                
            
                
                
                
            
            
                
                    
            
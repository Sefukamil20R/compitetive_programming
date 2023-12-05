class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        
        for i in range(len(order)):
            dic[order[i]] = i
        for i in range(len(words) - 1):
            size=min(len(words[i]),len(words[i+1]))
            for j in range(size):
                x = words[i]
                y = words[i + 1]
                if dic[x[j]] < dic[y[j]]:
                    break
                elif dic[x[j]] == dic[y[j]]:
                    continue
                else:
                    return False
            else:
                if len(words[i]) != size:
                    return False
                
        return True
                
            
                
                
       
    
            
            
        
        
        
            
             
            
                
            
             
        
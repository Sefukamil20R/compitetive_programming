class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count=Counter(s1)
        k=len(s1)
        window=Counter(s2[:k])
        if s1count==window:
            return True
        for i in range(1,len(s2)-k+1):
            window[s2[i-1]]-=1
            if window[s2[i-1]]==0:
                del window[s2[i-1]]
            window[s2[i+k-1]]+=1
            if window==s1count:
                return True 
        return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # S1count=Counter(s1)
        # k=len(s1)
        # window=Counter(s2[:k])
        # if window==S1count:
        #     return True 
        # for i in range(len(s2)-k):
        #     window[s2[i]]-=1
        #     if window[s2[i]]==0:
        #         del window[s2[i]]
        #     window[s2[i+k]]+=1
        #     if window ==S1count:
        #         return True
        # return False    

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #    S1count = Counter(s1)
    #    window=  Counter(s2[:len(s1)])
    #    if window == S1count:
    #        return True 
    #    k=len(s1)
    #    for i in range(1,len(s2)-k+1):
    #        window[s2[i-1]]-=1
    #        if window[s2[i-1]]==0:
    #            del window[s2[i-1]]
    #        window[s2[i+k-1]]+=1
    #        if window ==S1count:
    #            return True

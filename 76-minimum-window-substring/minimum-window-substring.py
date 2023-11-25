class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window,Tcount={},{}
        for c in t:
            Tcount[c]=Tcount.get(c,0) + 1
        l=0
        res=[-1,-1]
        reslength= float("inf")
        have,need=0,len(Tcount)
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in Tcount and window[c]==Tcount[c]:
                have+=1
                while have == need:
                      if (r-l+1) < reslength:
                          res=[l,r]
                          reslength=r-l+1
                      window[s[l]]-=1
                      if s[l] in Tcount and window[s[l]] < Tcount[s[l]]:
                          have-=1
                      l+=1
        l,r=res
        return s[l:r+1] if reslength!=float("inf") else ""
                       

                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
    

      
        
      
       
                        
        



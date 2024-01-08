class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
         k = len(p)
         pcount =  Counter(p)
         ind = k - 1
         ans = []
         Scount = Counter (s[:ind])
         while ind < len(s):
              Scount[s[ind]] += 1
              if pcount == Scount:
                  ans.append(ind-k+1)
              Scount[s[ind-k+1]] -= 1
              if Scount[s[ind-k+1]] == 0:
                 del Scount[s[ind-k+1]]
              ind += 1
         return ans 

        



           
                                                                   

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # pcount=Counter(p)
        # k=len(p)
        # window=Counter(s[:k])
        # ans=[]
        # if window==pcount:
        #     ans.append(0)
        # for i in range(1,len(s)-k+1):
        #     window[s[i-1]]-=1
        #     if window[s[i-1]]==0:
        #        del window[s[i-1]]
        #     window[s[i+k-1]]+=1
        #     if window==pcount:
        #         ans.append(i)
        # return ans



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #  pcount=Counter(s1)
        #  k=len(p)
        #  ans=[]
        #  window=Counter(s[:k])
        #  if pcount==Scount:
        #      ans.append(0)
        #  for i in range(len(s)-k):
        #        window[s[i]]-=1
        #        if  window[s[i]]==0:
        #            del window[s[i]]
        #        window[s[i+k]]+=1
        #        if window==pcount:
        #            ans.append(i+1)
        #  return ans            
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if len(p)>len(s):
        #     return([])
        # right=len(p)-1
        # anagram=[]
        # scount=Counter(s[0:len(p)-1])
        # pcount=Counter(p)
        # while right<len(s):
        #     scount[s[right]]+=1
        #     if scount==pcount:
        #         anagram.append(right-len(p)+1)
        #     scount[s[right-len(p)+1]]-=1
        #     if scount[s[right-len(p)+1]]==0:
        #         del scount[s[right-len(p)+1]]
        #     right+=1
        # return(anagram)  
        
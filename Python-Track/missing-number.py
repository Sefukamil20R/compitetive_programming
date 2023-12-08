class Solution:
    def missingNumber(self, nums: List[int]) -> int:
                n=len(nums)
                ans=[False]*(n+1)                
                for i in nums:
                    ans[i]=True
                for j in range(len(nums)+1):
                    if ans[j]==False:
                        return j
                      
       

            
                  
        
            
                
                    
                    
                    
                 
                    
                 
                
        
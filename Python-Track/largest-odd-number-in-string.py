class Solution:
    def largestOddNumber(self, num: str) -> str:
                 if int(num[-1])%2==1:
                        return num
                 else:
                    for i in range(len(num)-2,-1,-1):
                         if int(num[i])%2==1:
                                return num[:i+1]
                    return ""

            
                    
            
           
                        
                    
                    
                    
                        
                
                 
                        
                
                
          
            
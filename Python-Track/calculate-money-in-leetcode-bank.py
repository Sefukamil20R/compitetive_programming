class Solution:
    def totalMoney(self, n: int) -> int:
            start=1
            end=8
            week=n//7
            reday=n%7
            res=0
            if n <7:
                res= sum(range(1,n+1))
            else:
                for _ in range(week):
                    res+=sum(range(start,end))
                    start+=1
                    end+=1
                for _ in range(reday):
                    res+=start
                    start+=1
            return res
                    
                                
                             
                            
                 
            
        
       
    
            
            
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            summ=0
            res=[]
            
            for num in nums:
                  if num %2==0:
                     summ+=num 
            for v,j in queries:
                if nums[j]%2==0:
                        summ-=nums[j]
                        if (nums[j]+v) %2==0:
                            summ+=(nums[j]+v)
                        nums[j]+=v
                        res.append(summ)
                        
                else:
                    if (nums[j]+v) %2==0:
                        summ+=(nums[j]+v)
                    nums[j]+=v
                    res.append(summ)
                # print(nums)
            return res
          
                          
            
                        
                        
                        
                 
            
                
                    
                
                
            
                        
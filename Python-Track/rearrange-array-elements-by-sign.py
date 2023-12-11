class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
                        pospoin=0
                        negpoin=1
                        ans=[0]*len(nums)
                        for num in nums:
                            if num >0:
                                ans[pospoin]=num
                                pospoin+=2
                            else:
                                ans[negpoin]=num
                                negpoin+=2
                        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#             pos=[]
#             neg=[]
#             ans=[]
#             for num in nums:
#                 if num < 0:
#                     neg.append(num)
#             for num in nums:
#                 if num > 0:
#                     pos.append(num)
            
#             print(pos)
#             print(neg)
#             for i in range(len(pos)):
#                 ans.append(pos[i])
#                 ans.append(neg[i])
#             return ans
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
            ans=[]
            count=Counter(nums)
            for i in count.keys():
                if count[i] > len(nums)//3:
                    ans.append(i)
            return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # n= len(nums)
            # app=n/3
            # res=[]
            # count=Counter(nums)
            # print(count)
            # for key,value in count.items():
            #     if value > app:
            #         res.append(key)
            # return res
                
                
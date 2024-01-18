class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        prefix = []
        postfix = []
       
        for i in range (len(nums)):
            total *= nums[i]
            prefix.append(total)
        total = 1
        for i in range(len(nums)-1 , -1 , -1):
            total *= nums[i]
            postfix.append(total)
        postfix.reverse()
        res = [postfix[1]]
        for i in range(1,len(nums)):
           
            if i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res

              

        
        
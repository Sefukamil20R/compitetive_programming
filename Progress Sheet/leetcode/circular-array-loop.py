class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        after = lambda a : (a+nums[a])%len(nums)
       
        for i in range(len(nums)):
            j = i
            seen = set()
            while j not in seen and nums[after(j)]*nums[j]>0:
                seen.add(j)
                j=after(j)
            print(seen)
            if j==i and len(seen)>1:
                return True
        
        return False
            
        
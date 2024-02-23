class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
     
        total = sum(nums)
        if total % p == 0:
            return 0  

        rem = total % p
        prefix = 0
        remstore = {0: -1}  
        minn  = len(nums)

        for i, n in enumerate(nums):
            prefix = (prefix + n) % p
            left = (prefix - rem) % p
            if left in remstore:
                minn = min(minn, i - remstore[left])
            remstore[prefix] = i

        return minn if minn != len(nums) else -1      
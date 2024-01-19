class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = []
        ans  = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        for i in range(len(prefix)):
            if prefix[i] - goal in count:
                ans +=  count[prefix[i]-goal]
            count[prefix[i]] += 1
        return ans
                  


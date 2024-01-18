class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        prefix = []
        total = 0
        ans = 0
        count[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        for i in range(len(nums)):
            if prefix[i] - k in count:
                ans += count[prefix[i]-k]
            count[prefix[i]] += 1 
        return ans
            

                                               
        
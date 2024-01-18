class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        ans = 0
        prefix = []
        count = defaultdict(int)
        count[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        print(prefix)
        for i in range(len(prefix)):
             if prefix[i]%k in count:
                   ans += count[prefix[i]%k]
             count[prefix[i]%k] += 1
        return ans

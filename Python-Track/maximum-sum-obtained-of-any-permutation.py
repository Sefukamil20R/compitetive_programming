class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        for start , end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1
      
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.sort(reverse= True)
        nums.sort(reverse = True)
        res = 0
        for i in range(len(nums)):
          res += prefix[i]*nums[i]
        return res % (10**9 + 7)

        
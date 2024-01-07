class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
          firstsum = sum (nums[:k])
          firstavg = float(f"{(firstsum/k):.5f}")
          maximumavg = firstavg
          for i in range (k , len(nums)):
              firstsum += nums[i]
              firstsum -= nums[i - k]
              avg = float(f"{(firstsum/k):.5F}")
              maximumavg = max (avg , maximumavg)
          return maximumavg 

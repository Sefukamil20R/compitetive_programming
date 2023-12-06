class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
            i=0
            output=[]
            ans=[]
            while i < len(nums):
                ans=[nums[i+1]]*nums[i]
                output.extend(ans)
                i+=2
            return output
                
                
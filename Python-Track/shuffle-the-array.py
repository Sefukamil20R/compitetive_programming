class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
            ans = []
            i = 0
            j = len(nums)//2
            while i!=len(nums)/2:
                    ans.append(nums[i])
                    ans.append(nums[j])
                    i+=1
                    j+=1
            return ans
            
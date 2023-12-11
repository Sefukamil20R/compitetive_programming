class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
            myhash={}
            for i in range(len(nums)):
                myhash[nums[i]]=i
            for i in range(len(operations)):
                    idx=myhash[operations[i][0]]
                    nums[idx]=operations[i][1]
                    myhash[operations[i][1]]=idx
                    myhash.pop(operations[i][0])
            return nums
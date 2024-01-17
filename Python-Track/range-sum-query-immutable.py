class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        summ = 0 
        for i in range(len(nums)):
            summ += nums[i]
            self.prefix.append(summ)

        

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prefix[left-1] if left > 0 else 0
        rightsum = self.prefix[right]
        return rightsum - leftsum
        # leftsum = self.prefix[left-1]
        # rightsum = self.prefix[right]
        # if left > 0 :
        #     return rightsum - leftsum
        # return rightsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
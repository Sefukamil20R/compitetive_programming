class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def pre(l,r,play):
            if play :
                if l==r:
                    return nums[l]
                left=pre(l+1,r,not play )+nums[l]
                right=pre(l,r-1 , not play)+nums[r]
                return max(left,right)
            else:
                if l==r:
                    return -nums[l]
                left =pre (l+1,r,not play )-nums[l]
                right=pre (l,r-1,not play )-nums[r]
                return min(left,right)
        return pre (0,len(nums)-1,True)>=0
             #it means if finally we get posetiv number it retuerns true
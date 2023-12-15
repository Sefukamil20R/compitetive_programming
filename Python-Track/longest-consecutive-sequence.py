class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            num_set=set(nums)
            check=set()
            maxx=0
            for num in nums:
                n=num
                if num not in check:
                    rp=0
                    lp=0
                    while (num+1) in num_set:
                        rp+=1
                        num+=1
                        check.add(num)
                    while (n-1) in num_set:
                        lp+=1
                        n-=1
                        check.add(n)
                    maxx=max(lp+rp+1,maxx)
            
            return maxx            
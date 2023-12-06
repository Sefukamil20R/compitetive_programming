class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
            maxper=0
            count=0
            nums.sort()
            for i in range(len(nums)-2):
                if nums[i] + nums[i+1] > nums[i+2]:
                    perimeter=nums[i] + nums[i+1] + nums[i+2]
                    count+=1
                    maxper=max(perimeter,maxper)
            if count==0:
                 return 0
            else:
                return maxper

                  
                        
                        
                        
            
                        
                        
                
        
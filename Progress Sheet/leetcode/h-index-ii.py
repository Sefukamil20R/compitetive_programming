class Solution:
    def hIndex(self, citations: List[int]) -> int:
            n = len(citations)
            left = 0
            right = len(citations)-1
            while left <= right:
               mid = (right + left)//2
               if citations[mid] < n - mid:
                    left = mid + 1
               elif citations[mid] > n - mid:
                   right = mid -1 
               else:
                   return citations[mid] 
            return n - left




        # n = len(citations) 
        # left =  -1
        # right = n - 1
        # if sum(citations) == 0:
        #      return 0
              
        # while left + 1  < right:
        #     mid = (left + right)//2
        #     if citations[mid] < n - mid:
        #           left = mid
        #     else:
        #         right = mid
        #     if citations[mid] == n - mid:
        #         return citations[mid]
        # return  n - right
        
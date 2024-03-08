class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        def helper (cell):
            i = cell//m
            j = cell % m
            return [i,j]
        left = -1
        right = n*m - 1 
        
        while left + 1 < right:
            mid = (left + right)//2
            val = helper(mid)
            if matrix[val[0]][val[1]]  > target:
                  right = mid
            elif matrix[val[0]][val[1]]  < target:
                  left = mid
            else:
                return True
            # print(val)
            # return True
       
        
        val2 = helper(right)
        if matrix[val2[0]][val2[1]] != target:
                return False
        else:
            return True
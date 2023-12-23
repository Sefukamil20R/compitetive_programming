class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(matrix[0])):
                 temp.append((matrix[j][i]))
                 print(temp)
            ans.append(temp[::-1])
        
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                matrix[i][j]=ans[i][j]
        
        

        
        
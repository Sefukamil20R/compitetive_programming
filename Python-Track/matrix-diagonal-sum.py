class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        i,j=0,0
        while i<= len(mat)-1 and j<=len(mat):
            summ+=mat[i][j]
            i+=1
            j+=1
        i,j=0,len(mat)-1
        while i <= len(mat)-1 and j>=0:
            summ+=mat[i][j]
            i+=1
            j-=1
        if len(mat)%2!=0:
            summ-=mat[len(mat)//2][len(mat)//2]
        return summ
        
        



        
        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diss=defaultdict(list)
        ans=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d=i+j
                diss[d]+=[mat[i][j]]
        print(diss)
        for key ,value in diss.items():
            if key%2==0:
                ans.extend(value[::-1])
            else:
                ans.extend(value)
        return ans
        
                 
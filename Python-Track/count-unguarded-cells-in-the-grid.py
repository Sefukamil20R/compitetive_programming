class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell = [[0]*n for i in range (m)]
        for i , j in guards:
            cell[i][j] = 3 
        for i , j in walls:
            cell[i][j] = 2
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        for i , j in guards:
            for h in d :
                 a , b = i + h[0] , j + h[1]
                 while 0 <= a < m and 0 <= b < n and cell[a][b] not in [2,3]:
                    cell[a][b] = 1
                    a += h[0]
                    b += h[1]
        count = 0
        for i in range (m):
            for j in range (n):
                count += (cell[i][j]==0)
        return count 
        


         




        
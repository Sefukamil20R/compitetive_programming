class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(-1,0),(0,-1),(1,0),(0,1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def back(row,col,idx):
            seen.add((row,col))
            if idx == len(word):
                  return True
            ans = False
            for r , c in dir:
                newr = r + row
                newc = c + col
               
                      
                if inbound(newr,newc) and (newr,newc) not in seen and board[newr][newc]== word[idx]:
                       ans =  ans or  back(newr , newc , idx + 1)
                       seen.discard((newr,newc)) 
            return ans
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    seen = set()
                    res = res or back(i,j,1)
        return res

                    
        
                      
        
        
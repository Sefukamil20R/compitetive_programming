class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def back(open,close):
            if len(path) == 2*n:
                ans.append("".join(path[:]))
                return 
            if open != n:
                path.append("(")
                back(open + 1,close)
                path.pop()
            
            if close < open:
                  path.append(")")
                  back(open,close + 1)
                  path.pop()
        back(0,0)
        return ans 

            
            

            
            
        
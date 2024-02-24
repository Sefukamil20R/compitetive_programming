class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == "(":
                  stack.append(char)
            else:
                score = 0
                while stack and  stack[-1] != "(":
                     score += stack[-1]
                     stack.pop()
                stack.pop()
                if score:
                    stack.append(2*score)
                else:
                    stack.append(1)
        return sum(stack)



                   
       


                     
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0 
        while i < len(tokens):
            if tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "/":
                 x = stack.pop()
                 y = stack.pop()
                 stack.append(int (y/x))
            elif tokens[i] == "-":
                 x = stack.pop()
                 y = stack.pop()
                 stack.append(int(y-x))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[-1]
            

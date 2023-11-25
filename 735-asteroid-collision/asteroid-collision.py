class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            
            while stack and stack[-1] > 0 and i < 0:
                 dif=stack[-1] + i
                 if dif>0:
                    i=0 
                 elif dif<0:
                     stack.pop()
                 else:
                       stack.pop() 
                       i=0
            if i:          
                stack.append(i)
        return stack
        
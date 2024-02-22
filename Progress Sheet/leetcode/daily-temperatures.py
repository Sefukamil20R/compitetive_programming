class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         stack = []
         res = [0]*len(temperatures)
         for i in range(len(temperatures)-1 ,  -1 , -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
         return res 
         

       














        #   ans = [] 
        #   l = 0
        #   r = 1
        #   count = 0
        #   while r < len(temperatures):
        #       if temperatures[r] > temperatures[l]:

        #              ans.append(r-l)
        #              l += 1
        #              r += 1
        #              r = l
                
        #       else:
        #           r += 1
        #   if len(ans) == len(temperatures):
        #       return ans
        #   else:
        #       diff = len(temperatures) - len(ans)
        #       for i in range(diff):
        #           ans.append(0)
        #       return ans 
          
                  
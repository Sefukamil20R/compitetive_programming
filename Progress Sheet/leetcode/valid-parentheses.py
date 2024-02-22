class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid ={
            ')' : '(',
            '}' : '{' ,
            ']' : '['
            } 
        for i in s:
           if i in valid:
               if stack and stack[-1] == valid[i]:
                   stack.pop()
               else:
                    return False

           else:
               stack.append(i)
        return len(stack) == 0



               
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #   stack=[]
    #   valid ={
    #          ')' : '(',
    #        '}' : '{' ,
    #       ']' : '['
    #          } 
    #   for i in s:
    #       if i in valid:
    #           if stack and stack[-1]==valid[i]:
    #               stack.pop()
    #           else:
    #              return False 
    #       else :
    #         stack.append(i)
    #   return True if not stack else False 



   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #  stack=[]
    #   valid ={
    #         ')' : '(',
    #        '}' : '{' ,
    #        ']' : '['
    #      } 
    #   for i in s:
    #          if i in valid.values():
    #              stack.append(i)
    #          elif stack and valid[i]==stack[-1]:
    #              stack.pop()
    #          else:
    #               return False
    #   return stack==[]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
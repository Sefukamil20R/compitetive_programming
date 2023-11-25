class Solution:
    def simplifyPath(self, path: str) -> str:
       stack=[]
       cur=""
       for c in  path + "/":
           if c=="/":
               if cur=="..":
                   if stack:
                       stack.pop()
               elif cur!="" and cur!=".":
                    stack.append(cur)
               cur=""
           else:
               cur+=c
       return "/" + "/".join(stack)

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # stack=[]
        # elements=path.split("/")
        # for c in elements:
        #     if c=="..":
        #         if stack :
        #             stack.pop()
        #     elif c!="" and c!=".":
        #         stack.append(c)
        # simplified="/" + "/".join(stack)
        # return simplified 

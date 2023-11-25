class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
         stack=[]
         for i in s:
            if not stack or stack[-1][0]!=i:
                 stack.append([i,1])   
            else:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
         res=""
         for char , count in stack:
            res+=char*count
         return res

                
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # stack=[]
        # for i in s:
        #     if stack and stack[-1][0]==i:
        #         stack[-1][1]+=1
        #     else:
        #         stack.append([i,1])
        #     if stack[-1][1]==k:
        #             stack.pop() // eziga ifu keneza if ekul new indent because ke else sir karegshiw else sisera bicha new ifn check miyaregew.
        # res=""
        # for char,count in stack:
        #     res+=(char*count)
        # return res
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lists = path.split("/")
        for char in lists:
            if char == "..":
                if stack:
                    stack.pop()
            elif char != "" and char != ".":
                  stack.append(char)
        return "/" + "/".join(stack)










    #   lists = path.split("/") 
    #   print(lists)
    #   stack = []
    #   for char in lists:
    #       if char != '' and char != "." and char != "..":
    #           stack.append(char)
    #       elif char == "..":
    #           if stack:
    #               stack.pop()
    #   print(stack)
    #   return "/" + "/".join(stack)
          

        
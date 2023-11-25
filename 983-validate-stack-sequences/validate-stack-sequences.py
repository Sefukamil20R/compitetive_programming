class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:  
    stack=[]
    i=0
    for c in pushed:
          stack.append(c)
          while  i<len(popped) and stack and stack[-1]==popped[i]:
              stack.pop()
              i+=1
    return  not stack
          
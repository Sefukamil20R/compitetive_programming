class Solution:
  def trap(self, height: List[int]) -> int:
    count = 0
    stack = []
    for i in range(len(height)):
        while stack and height[stack[-1]] <= height[i]:
            val = stack.pop()
            if stack:
                h = min( height[stack[-1]] ,  height[i] ) - height[val] 
                w = i - (stack[-1] + 1)
                count += h*w
        stack.append(i)
    return count
                
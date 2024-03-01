# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        add = 0
        def sumup(root , add):
            nonlocal ans
            if not root:
                return 
            add +=  root.val
            
            if not root.left and not root.right:
                ans += add 
                return 
            sumup(root.left , add*10)
            sumup(root.right , add*10)
        sumup(root , add)
        return ans 


                

        
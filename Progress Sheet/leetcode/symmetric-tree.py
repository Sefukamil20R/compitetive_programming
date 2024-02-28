# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p,q):
            if p and q:
               
                if p.val==q.val:
                    return check(p.left , q.right) and check(p.right , q.left)
                return False 
            else:
                if not p and not q:
                    return True
                else:
                    return False
        p , q = root , root
        ans = check(p,q)
        return ans
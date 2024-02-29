# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def maximum (root):
            nonlocal ans
            if not root:
                return [float("inf"), float("-inf")]

            left = maximum(root.left)
            right = maximum(root.right)

            minn = root.val - min(left[0], right[0])
            maxx = max(right[1], left[1]) - root.val
       
            ans = max(ans, minn , maxx)
        

            return [min(left[0], right[0], root.val), max(right[1], left[1], root.val)]
        maximum(root)
        return ans



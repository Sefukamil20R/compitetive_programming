# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            def searching (root , p ,q):
                if p.val > root.val and q.val > root.val:
                        return searching(root.right,p ,q)
                elif p.val < root.val and q.val < root.val:
                        return searching(root.left ,p ,q)
                elif p.val == root.val:
                    return p
                elif q.val == root.val:
                    return q
                else:
                    return root
            return searching(root,p,q)

                
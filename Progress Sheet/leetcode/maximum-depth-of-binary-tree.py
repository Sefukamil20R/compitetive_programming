# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return 1 + max(self.maxDepth(root.right) , self.maxDepth(root.left)) if root else 0
        def find_max(root):
                if not root : 
                    return 0
                left = 1 + find_max(root.left)
                right = 1 + find_max(root.right)
                return max(left,right)
        return find_max(root)









        # ans = []
        # def depth(root):
        #     count = 0
        #     if root:
        #         count += 1
        #         ans.append(count)
        #         depth(root.left)
        #         depth(root.right)
            
                
        # depth(root)
        # return len(ans)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(l,r):
            if r == l:
                return TreeNode(nums[l])
            if l > r:
                  return  
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            leftsub = BST(l , mid-1)
            rightsub = BST(mid+1,r)
            root.left = leftsub
            root.right = rightsub
            return root
        return BST(0,len(nums)-1)


        
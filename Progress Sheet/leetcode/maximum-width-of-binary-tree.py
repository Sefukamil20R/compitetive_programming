# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        widths =  defaultdict(list)
        def back(root,level,formula):
             if root:
                widths[level].append(formula)
                back(root.left,level+1,2*formula+1)
                back(root.right,level +1 ,2*formula + 2)
        back(root,0,0)
        ans = 0
        for key,val in widths.items():
            ans = max(ans,max(val) - min(val) + 1) 
        return ans


















        # widths = defaultdict(list)
        # def back(root,level,formula):
        #     if root:
        #         widths[level].append(formula)
        #         print(formula)
        #         back(root.left,level+1,2*formula+1)
        #         back(root.right,level+1,2*formula+2)
        # back(root,0,0)
        # res = 0
        # print(widths)
        # for k , v in widths.items():
        #     res = max(res , max(v) - min(v)+1)
        # return res 

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
                levelO = defaultdict(list)
                lev = 0
                ans = []
                def checker(root , lev):
                    if root:
                        levelO[lev].append(root.val)
                        checker(root.right , lev + 1)#1
                        checker(root.left , lev + 1)
                       
                checker(root,0)
                for key , val  in levelO.items():
                    if key % 2== 0:
                        ans.append(val[::-1])
                    else:
                        ans.append(val)
                print(levelO)
                return ans
                




           


        
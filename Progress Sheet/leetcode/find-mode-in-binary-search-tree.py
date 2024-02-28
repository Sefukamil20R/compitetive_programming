# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # visited = defaultdict(int)
        # res  = 0
        # ans = []
        # if not  root:
        #     return None
        # stack = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     visited[node.val] += 1
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # res = max(visited.values())
        # for i in visited:
        #     if visited[i] == res:
        #         ans.append(i)
        # return ans
        ans = []
        temp = defaultdict(int)
        def counters(root):
            if root:
                temp[root.val] += 1
                counters(root.left)
                counters(root.right)
        counters(root)
        maxx = max(temp.values())
        for i in temp:
                    if temp[i] == maxx:
                        ans.append(i)
        return ans



        
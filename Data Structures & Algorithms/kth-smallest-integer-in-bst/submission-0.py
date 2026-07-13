# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        # Could do DFS or BFS and add all the node.val into a list and then get the kth smallest
        # I feel like a fast and more efficient way is possible since it is a BST

        values = []

        def dfs(node):

            nonlocal values

            if not node:
                return
            else:
                values.append(node.val)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            return 

        dfs(root)

        values.sort()

        return values[k - 1]
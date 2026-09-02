# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        # Go down each branch (DFS) and swap the left and right node
        # We would need an `if` statement to make sure the node has a l and r

        def dfs(node):

            node.right, node.left = node.left, node.right

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            return node

        return dfs(root)

            



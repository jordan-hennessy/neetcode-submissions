# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
            # I am thinking this is a DFS
            # I think we compare the current value of the node to it's children
            # We would probably use a counter `nonlocal`
            # An extra function is needed to go deeper everytime

        # Counter
        res = 0

        def dfs(node, max_seen):
            # Bring the counter in
            nonlocal res

            if not node:
                return

            # Add to counter
            if max_seen <= node.val:
                res += 1

            max_seen = max(max_seen, node.val)

            if node.left:
                dfs(node.left, max_seen)
            if node.right:
                dfs(node.right, max_seen)


        dfs(root, float('-inf'))

        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            
            # If p and q are split then the current node is the deepest
            # If p and q are on the same side, we can go deeper
            # We must check the current node first as that might be one that we are searching for. 
            # If the current node is p or q that is also the deepest. (This must be after the first steps)

        # Check if p and q are split
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root

        # If p and q are on the same side, we can go deeper
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If the current node is p or q that is also the deepest.
        if root.val == p.val or root.val == q.val:
            return root

        

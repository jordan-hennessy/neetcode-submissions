# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if node is None:
                return None
            left_inverted = invert(node.left)
            right_inverted = invert(node.right)
            node.left = right_inverted
            node.right = left_inverted
            return node
        
        return invert(root)
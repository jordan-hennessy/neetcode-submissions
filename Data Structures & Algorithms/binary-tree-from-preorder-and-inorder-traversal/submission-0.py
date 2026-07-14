# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # First number in `preorder` is always root
        # Once we know the root, anything to the left of the root in `inorder` is in left subtree
        # Anything after root is in right subtree
        # 


        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        left_inorder = inorder[:mid]
        gap = len(left_inorder)
        left_preorder = preorder[1: 1 + gap]

        right_inorder = inorder[mid + 1:]
        right_preorder = preorder[1 + gap:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root


        
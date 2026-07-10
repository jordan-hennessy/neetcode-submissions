# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

            # I think both BFS and DFS would work
            # We are checking each nodes childrens values
            # Should we check the children first?
            # if yes then we will have to make sure it has children

        isBinary = True

        def dfs(node, low, high):

            nonlocal isBinary

            if not node:
                return
            
            if node.val <= low or node.val >= high:
                isBinary = False
                return

    
            if node.left:
                dfs(node.left, low, node.val)
            
            if node.right:
                dfs(node.right, node.val, high)

        dfs(root, float('-inf'), float('inf'))

        return isBinary

            


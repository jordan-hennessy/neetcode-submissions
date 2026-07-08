# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

            # Uses BFS 
            # We want to create a list of every number on each layer.
            # Can't fully remember how to do BFS, but I know what it is
            # Add numbers on a layer to a list and append that list to a result list before moving onto the next layer
            # The values don't matter to us here.
            # A node might be None but there could be more nodes in the tree on that level.
        
        res = []

        if not root:
            return []
        
        queue = [root]
        layer = []

        while queue:

            layer_size = len(queue)

            for i in range(layer_size):
                node = queue.pop(0)
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(layer)
            layer = []

        return res




            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

            # Seems like another BFS
            # We can got layer by layer and only use the last value in the queue
            # can only be one node on the right per layer

            # FOR LOOP:
            # - add all nodes to the level list
            # - only add the last node from level into res
            # - 

        if not root:
            return []

        res = []
        queue = deque([root])
        level = []

        while queue:

            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level[-1])
            level = []

        return res


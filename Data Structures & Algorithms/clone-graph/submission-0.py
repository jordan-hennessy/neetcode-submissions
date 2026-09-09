"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        newToOld = {}

        def dfs(node):
            if node in newToOld:
                return newToOld[node]   # give back the new node if it exists
            
            copy = Node(val=node.val)   # create the new node (old val), no neighbors yet
            newToOld[node] = copy       # assign it in the dict

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy


        return dfs(node) if node else None

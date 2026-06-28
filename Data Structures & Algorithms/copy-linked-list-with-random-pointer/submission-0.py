"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None


        mapping = dict()

        curr = head

        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = mapping[curr]
            copy.next = mapping.get(curr.next)
            copy.random = mapping.get(curr.random)
            curr = curr.next
        
        return mapping[head]
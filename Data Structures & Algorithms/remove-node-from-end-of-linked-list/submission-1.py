# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nth = head
        curr = head

        dummy = ListNode(0)
        dummy.next = head

        for _ in range(n):
            curr = curr.next

        # move both together till curr is no more
        prev = dummy

        while curr:
            prev = prev.next
            nth = nth.next      # might be an issue with small lists
            curr = curr.next
        
        # Nth will be nth from the end
        prev.next = nth.next

        return dummy.next
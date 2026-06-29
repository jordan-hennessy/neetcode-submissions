# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return None

        dummy = ListNode(0)
        newList = dummy
        
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sum = val1 + val2 + carry
            
            newList.next = ListNode(sum % 10)
            newList = newList.next

            carry = sum // 10

            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0

        return dummy.next
        


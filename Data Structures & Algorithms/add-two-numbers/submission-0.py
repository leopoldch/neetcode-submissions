# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        head1, head2 = l1, l2
        dummyNode = ListNode()
        last = dummyNode
        while head1 or head2:

            total = carry
            if head1 and head2:
                total += head1.val+ head2.val
                head1 = head1.next
                head2 = head2.next
            elif head1:
                total += head1.val
                head1 = head1.next
            else:
                total += head2.val
                head2 = head2.next
            
            carry = total // 10
            new_node = ListNode(total-carry*10)
            last.next = new_node
            last = new_node
            
        if carry:
            new_node = ListNode(carry)
            last.next = new_node

        return dummyNode.next


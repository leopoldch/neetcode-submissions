# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None

        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        
        dummyNode = ListNode(next=head)
        last = dummyNode
        current = head
        
        for _ in range(length-n):
            last, current = current, current.next
        
        last.next = current.next

        return dummyNode.next



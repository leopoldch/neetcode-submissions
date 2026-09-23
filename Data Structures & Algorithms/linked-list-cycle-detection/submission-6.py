# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        pt = head
        fast = head

        while fast != None:
            pt = pt.next

            if fast.next == None:
                return False

            fast = fast.next.next

            if pt == fast:
                return True
        
        return False

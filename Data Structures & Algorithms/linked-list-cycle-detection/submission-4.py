# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        min_val = 1001
        max_val = -1001

        if head == None:
            return False

        while head.next != None:
            if min_val == head.val or max_val == head.val:
                return True

            if min_val > head.val:
                min_val = head.val
            if max_val < head.val:
                max_val = head.val

            head = head.next

        return False
            
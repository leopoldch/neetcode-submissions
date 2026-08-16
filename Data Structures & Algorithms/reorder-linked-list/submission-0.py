# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stored_head = head
        queue = deque();current = head

        while current != None:
            queue.append(current)
            current = current.next

        queue.popleft()
        current = stored_head
        back = True

        while queue:
            if back:
                node = queue.pop()
            else:
                node = queue.popleft()
            
            current.next = node
            current = current.next
            back = not back 

        current.next = None 


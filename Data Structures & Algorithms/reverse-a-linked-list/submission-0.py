# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        if head == None:
            return head

        while head.next != None:
            tmp = head.next 

            head.next = prev
            prev = head

            head = tmp


        head.next = prev

        return head



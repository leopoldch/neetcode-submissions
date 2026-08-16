# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        if list1 == None:
            return list2
        if list2 == None:
            return list1
        

        head = None
        other = None
        start = None

        if list1.val < list2.val:
            head = list1
            other = list2
            start = list1
        else:
            head = list2
            other = list1
            start = list2


        while other != None and head.next != None:
            if other.val > head.next.val:
                head = head.next
                continue
            
            tmp = head.next
            tmp2 = other.next
            other.next = tmp
            head.next = other
            other = tmp2

            
        
        if head.next == None and other != None:
            head.next = other


        return start
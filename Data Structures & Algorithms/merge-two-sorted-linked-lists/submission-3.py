# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1, )
        
        if list1: 
            dummyNode.next = list1
        else:
            return list2
        
        current = dummyNode

        while list2:

            tmp = current.next

            if not tmp:
                current.next = list2
                break
            
            if tmp.val < list2.val:
                current = current.next
                continue

            list2_next = list2.next

            current.next = list2
            current.next.next = tmp

            list2 = list2_next

        return dummyNode.next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        # 1. Trouver le milieu
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Inverser la deuxième moitié
        # On coupe d'abord la liste en deux
        second_half = slow.next
        slow.next = None 
        
        prev = None
        curr = second_half
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # 3. Fusionner les deux listes (head et prev)
        first, second = head, prev
        while second: # La deuxième liste est toujours plus courte ou égale
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
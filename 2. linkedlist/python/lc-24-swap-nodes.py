class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        a = head
        b = a.next
        d = None
        while a and b:
            b = a.next
            c = b.next
            b.next = a
            if d:
                d.next = b
            else:
                head = b
            d = a
            a = c
        return head
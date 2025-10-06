def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or not head.next or left == right:
        return head

    prev = None
    slow = head
    count = 1

    #Reach till left
    while count < left:
        prev = slow
        slow = slow.next
        count += 1

    #Save edge pointers for later
    x = prev
    y = slow

    #Reverse till right
    tempnext = None
    while count <= right:
        tempnext = slow.next
        slow.next = prev
        prev = slow
        slow = tempnext
        count += 1
    
    #Set edge pointers to correct next node
    if not x:
        head = prev
    else:
        x.next = prev    
    
    y.next = tempnext

    return head
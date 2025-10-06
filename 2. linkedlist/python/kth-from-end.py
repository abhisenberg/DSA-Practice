class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def kthFromEnd(head, k):
    fast = head
    slow = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    print(slow.val)

kthFromEnd(head, 4)


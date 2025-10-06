class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def iterate(node):
    if not node:
        return
    
    print(node.val, " -> ")
    iterate(node.next)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

iterate(head)


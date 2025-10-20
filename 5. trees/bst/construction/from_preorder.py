from ..bst import Node

def from_preorder(parr):    #preorder array passed as input
    if not parr:
        return None

    root = parr[0]
    i = 1

    while i < len(parr) and parr[i] < root:
        i += 1
    
    root_node = Node(root)
    root_node.left = from_preorder(parr[1:i])
    root_node.right = from_preorder(parr[i:])
    return root_node

if __name__ == "__main__":
    print(from_preorder([10,5,4,8,6,7,13,11,12,18]))

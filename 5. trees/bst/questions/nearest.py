from ..bst import Node
from ..construction.from_preorder import from_preorder
from bisect import bisect_left

# def findFloorAndCeil(node, target, floor, ceil):
#     if not node:
#         return floor, ceil
    
#     if node.val == target:
#         return target, target
    
#     if target < node.val:
#         return findFloorAndCeil(node.left, target, floor, node.val)
    
#     return findFloorAndCeil(node.right, target, node.val, ceil)

# tree = from_preorder([6,2,1,4,13,9,15,14])
# print(tree)
# print(findFloorAndCeil(tree, 7, None, None))

def main():

    tree = from_preorder([6,2,1,4,13,9,15,14])

    intrav = []
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        intrav.append(node.val)
        inorder(node.right)
    
    inorder(tree)
    print(intrav)

    target = 16

    i = bisect_left(intrav, target)

    if i == len(intrav):
        return [intrav[-1], -1]
    
    if intrav[i] == target:
        return [target, target]
    
    if i == 0:
        return [-1, intrav[0]]
    
    return [intrav[i-1], intrav[i]]

print(main())
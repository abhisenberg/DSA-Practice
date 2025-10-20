from collections import deque

class Node():
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.level_order_str()

    def level_order_str(self) -> str:
        q = deque([self])
        ans = []
        while q:
            node = q.popleft()

            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("-")

        return " ".join(ans)
    
if __name__ == "__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)

    print(root)

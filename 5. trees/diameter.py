class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diam = 0
        def dia(node):
            nonlocal diam

            if not node:
                return 0

            left_branch_len = dia(node.left)
            right_branch_len = dia(node.right)

            diam = max(left_branch_len + right_branch_len+ 1, diam)

            return max(left_branch_len, right_branch_len) + 1

        dia(root)
        return diam-1


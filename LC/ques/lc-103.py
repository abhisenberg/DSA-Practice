class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)

        ltr = True
        ans = []

        while q:
            nicl = len(q)
            
            #Create a deque so that we can insert the values at any end
            level_list = collections.deque()
            while nicl:
                node = q.popleft()
                if ltr:     #If LTR, insert at the end
                    level_list.append(node.val)
                else:       #If not LTR, insert at the start
                    level_list.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                nicl -= 1

            #Insert current level's answer 
            ans.append(level_list)
            ltr = not ltr
        
        return ans
    
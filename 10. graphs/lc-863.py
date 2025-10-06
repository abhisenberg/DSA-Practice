class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #1. Convert the BT to a graph
        graph = defaultdict(list)
        
        def traverse(node, parent):     
            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
                traverse(node.left, node)
            if node.right:
                graph[node.val].append(node.right.val)
                traverse(node.right, node)
        
        traverse(root, None)
        
        #2. Perform BFS to find distance K nodes
        level = 0
        q = deque()
        seen = set()
        ans = []

        q.append(target.val)
        seen.add(target.val)

        while q:
            nicl = len(q)
            for _ in range(nicl):
                node = q.popleft()
                if level == k:
                    ans.append(node)
                else:
                    for nbr in graph[node]:
                        if nbr not in seen:
                            seen.add(nbr)
                            q.append(nbr)
            level += 1

        return ans


            

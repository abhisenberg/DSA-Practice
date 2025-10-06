class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1:
            return -1

        #1. Define the directions
        directions = [(-1,-1), (-1,0), (0,-1), (0,1), (1,0), (1,1), (-1,1), (1,-1)]

        #2. Helper function to check coordinates are valid
        def isvalid(i, j):
            return 0 <= i < n and 0 <= j < n and grid[i][j] == 0
        
        #3. Write the BFS
        level = 1
        q = deque()
        q.append((0,0))
        seen = set()
        seen.add((0,0))
        
        while q:
            nicl = len(q)

            for _ in range(nicl):
                x, y = q.popleft()
                if x == n-1 and y == n-1:   #Check if current node is the answer
                    return level
                
                for dx, dy in directions:   #Add next set of neighbours to queue
                    nextx, nexty = dx+x, dy+y
                    if isvalid(nextx, nexty) and (nextx, nexty) not in seen:
                        seen.add((nextx, nexty))
                        q.append((nextx, nexty))
                
            level += 1

        return -1        


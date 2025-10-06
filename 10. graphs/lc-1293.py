class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        #0. Define helper function to check validity and directions
        def isvalid(i,j):
            return 0 <= i < m and 0 <= j < n
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        #1. Define queues and other relevant variables
        q = deque()
        seen = set()
        lvl = 0 #This is the number of steps taken to reach the destination

        q.append((0,0,k))   #The initial state of the starting point
        seen.add((0,0,k))

        #2. Run DFS
        while q:
            nicl = len(q)
            
            for _ in range(nicl):
                i, j, removal = q.popleft()

                if i == m-1 and j == n-1:
                    return lvl
                
                for dx, dy in directions:
                    x, y = i+dx, j+dy
                    if isvalid(x,y) and removal >= grid[i][j] and (x,y,removal-grid[i][j]) not in seen:
                        q.append((x,y,removal-grid[i][j]))
                        seen.add((x,y,removal-grid[i][j]))
            
            lvl += 1

        #3. If the function has not returned yet then it means there is not way to reach the end
        return -1
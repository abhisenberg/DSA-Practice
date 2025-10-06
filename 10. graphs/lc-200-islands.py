class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        #Helper: Check if the indices are valid for the given grid
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
            
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()

        #Write the DFS logic
        def dfs(i, j):
            for dx, dy in directions: #Iterating over neighbours
                x, y = i+dx, j+dy
                if isValid(x,y) and grid[x][y] == '1' and (x,y) not in seen:
                    seen.add((x,y))
                    dfs(x, y)
        
        #Calculating number of islands i.e. connected components
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    seen.add((i, j))
                    ans += 1
                    dfs(i, j)
        
        return ans
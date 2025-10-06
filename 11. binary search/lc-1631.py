from typing import List

def minimumEffortPath(heights: List[List[int]]) -> int:
    #0. Figure out the lowest and highest effort possible
    left = 0 #Lowest effort = 0 if all cells have same value
    right = max(max(row) for row in heights) #Highest effort = max value present in the matrix

    #1. Write a function that checks whether there is a path in graph with effort k
    m, n = len(heights), len(heights[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    def isValid(r, c):
        return 0 <= r < m and 0 <= c < n
    

    def check(k):
        seen = set()
        seen.add((0,0))

        def dfs(x, y):
            if x == m-1 and y == n-1:
                return True
            
            possible = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isValid(nx,ny) and (nx,ny) not in seen:
                    if abs(heights[nx][ny]-heights[x][y]) <= k :
                        seen.add((nx,ny))
                        possible = possible or dfs(nx, ny)
            
            return possible

        return dfs(0, 0)
    
    #2. Use binary search to search for the minimum effort required
    while left <= right:
        mid = (left + right) // 2
        print("Checking for effort = ", mid)
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


arr = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

print(minimumEffortPath(arr))
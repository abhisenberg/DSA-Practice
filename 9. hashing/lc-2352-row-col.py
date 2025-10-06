from typing import List
from collections import defaultdict

def equalPairs(grid: List[List[int]]) -> int:
    #Create the hm of rows
    rowhm = defaultdict(int)
    for row in grid:
        rowhm[tuple(row)] += 1
    
    #Create the hm of columns
    colhm = defaultdict(int)
    n = len(grid)
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])
        colhm[tuple(col)] += 1

    print("rowhm: ", rowhm)
    print("colhm: ", colhm)
    
    #Calculate total number of pair of row-cols
    ans = 0
    for r in rowhm:
        ans += rowhm[r] * colhm[r]
    return ans

print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
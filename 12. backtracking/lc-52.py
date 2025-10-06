class Solution:
    def totalNQueens(self, n: int) -> int:
        
        #0. Create sets to store the attackable cols, diagonals and anti-diagonals
        attackable_cols = set()
        attackable_dias = set()
        attackable_anti_dias = set()

        #1. Create helper function to mark attackable positions if a queen is placed at (r,c)
        def putQueen(r,c):
            attackable_cols.add(c)
            attackable_dias.add((r-c))
            attackable_anti_dias.add((r+c))

        #2. Create helper function to remove attackable positions if a queen is remove from (r,c)
        def removeQueen(r,c):
            attackable_cols.remove(c)
            attackable_dias.remove((r-c))
            attackable_anti_dias.remove((r+c))

        #3. Create helper function to check if a positions is valid
        def isValid(r,c):
            return c not in attackable_cols and (r-c) not in attackable_dias and (r+c) not in attackable_anti_dias

        #4. Backtracking function
        ans = 0
        def nqueen(row):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for col in range(0, n):
                if isValid(row, col):
                    putQueen(row, col)
                    nqueen(row+1)
                    removeQueen(row, col)
        
        nqueen(0)
        return ans

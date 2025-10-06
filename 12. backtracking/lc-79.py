class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #0. Define helper functions for checking valid and directions
        m = len(board)
        n = len(board[0])
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        #1. Define backtracking function
        seen = set()
        def wordSearch(row, col, i):    #'i' is the current alphabet we are looking for
            if i == len(word):  #If we run out of alphabets, we have found all letters of the world
                return True

            for dx, dy in dirs:
                x, y = row + dx, col + dy
                if isValid(x,y) and (x,y) not in seen:
                    if board[x][y] == word[i]:  #Check if the cell we are considering matches with the letter we are currently looking for
                        seen.add((x,y))
                        isFound = wordSearch(x,y,i+1) #We found current alphabet, move to next alphabet finding
                        if isFound:
                            return True

                        seen.remove((x,y))

            return False

        #2. Since we don't have a fixed starting point, we will iterate through all starting positions possible
        for row in range(0, m):
            for col in range(0, n):
                if word[0] == board[row][col]:
                    seen.add((row, col))
                    isFound = wordSearch(row, col, 1)   #Start by searching the next alphabet
                    if isFound:
                        return True
                    seen.remove((row, col))
        
        return False
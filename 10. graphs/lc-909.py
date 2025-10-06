from typing import List
from collections import deque
import math

def snakesAndLadders(board: List[List[int]]) -> int:
    n = len(board)

    #1. Define helper functions to convert between labels and indices
    def getlabel(i, j):
        x = n-i
        if x % 2 == 0: #If even
            return 6*(x-1) + (6-j)
        else: #If odd
            return 6*(x-1) + (j+1)
    
    def getindices(label):
        i = n - (math.ceil(label / n))
        
        j = -1
        if not (n - i) % 2: #For an even row from bottom
            if not label % n:
                j = 0
            else:
                j = n - (label % n)
        else:   #For an odd row from bottom
            if not label % n:
                j = n-1
            else:
                j = (label % n) - 1

        return (i, j)

    def getnextmoves(label):
        moves = []
        for i in range(label+1, min(label+6, n*n)+1):
            moves.append(i)
        return moves

    #2. Perform BFS
    q = deque()
    seen = set()

    q.append(1)
    seen.add(1)

    lvl = 0
    while q:
        nicl = len(q)

        for _ in range(nicl):
            curr = q.popleft()

            if curr == n*n:
                return lvl
            
            nextmoves = getnextmoves(curr)
            for move in nextmoves:
                mi, mj = getindices(move)
                if board[mi][mj] != -1:
                    move = board[mi][mj]
                
                if move not in seen:
                    print("For ", curr, ", Adding move: ", move)
                    seen.add(move)
                    q.append(move)

        lvl += 1
    
    return -1

board = [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]
ans = snakesAndLadders(board)
print(ans)
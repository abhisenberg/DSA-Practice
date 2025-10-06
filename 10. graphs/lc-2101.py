import math
from collections import defaultdict
from typing import List

def maximumDetonation(bombs: List[List[int]]) -> int:
        
        #0. Contains the mapping of i-th bomb against the list of bombs that it'll detonate
        graph = defaultdict(list)

        #1. Get the next set of bombs that will be detonated
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                a, b, r1 = bombs[i]
                x, y, r2 = bombs[j]
                d = math.sqrt((a-x)**2 + (b-y)**2)
                if r1 >= d:
                    graph[i].append(j)
                if r2 >= d:
                    graph[j].append(i)

        """2. Run DFS
        My original solution of keeping the already detonated answers in "chainlist" will NOT work,
        because there are bombs that mutually detonate each other, and we want to see the max chain length
        when the current bomb is the absolute source of the detonation of that chain.
        And if we store data in "chainlist", the bomb is NOT the source of the detonation and the stored answer could be smaller
        than the actual answer.
        """
        def dfs(i, seen):
            for nbr in graph[i]:
                if nbr not in seen:
                    seen.add(nbr)
                    dfs(nbr, seen)
            
            #We can use a variable "chain" that adds up each bomb in the chain,
            #or we can just use the length of "seen" since it's the same thing
            return len(seen)    
        
        maxchain = 0
        for i in range(len(bombs)):
            maxchain = max(dfs(i, set([i])), maxchain)
        
        return maxchain


test1 = [[2,1,3],[6,1,4]]
print(maximumDetonation(test1))

test2 = [[1,1,5],[10,10,5]]
print(maximumDetonation(test2))

test3 = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(maximumDetonation(test3))
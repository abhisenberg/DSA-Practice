from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # Convert it into a graph
    graph = defaultdict(dict)
    for i in range(len(equations)):
        x, y = equations[i]
        v = values[i]
        
        graph[x][y] = v
        graph[y][x] = 1/v
        
        graph[x][x] = 1
        graph[y][y] = 1
    
    # Query solving
    def query(node, target):
        stack = [(node, 1)]
        vis = set()
        vis.add(node)
        while stack:
            x, xv = stack.pop()
            for nbr in graph[x]:
                nbrv = graph[x][nbr]

                if x == target:
                    return xv
                
                if nbr not in vis:
                    vis.add(nbr)
                    stack.append((nbr, xv * nbrv))
        return -1

    # for each query, run a DFS to find the answer
    ans = []
    for p, q in queries:
        ans.append(query(p, q))

    print(ans)

    pass


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

calcEquation(equations, values, queries)
import math
from collections import defaultdict, deque
from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    #1. Create a graph
    graph = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            graph[pattern].append(word)

    print(graph)

    def nextwords(word):
        list_ = []
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            for nword in graph[pattern]:
                list_.append(nword)
        return list_
    
    #2. Perform BFS
    q = deque()
    seen = set()

    q.append(beginWord)
    seen.add(beginWord)

    lvl = 1
    while q:
        nicl = len(q)
        for _ in range(nicl):
            word = q.popleft()
            
            if word == endWord:
                return lvl
            
            nwords = nextwords(word)
            for nword in nwords:
                if nword not in seen:
                    print("From {} going to {}".format(word, nword))
                    seen.add(nword)
                    q.append(nword)

        lvl += 1
    
    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
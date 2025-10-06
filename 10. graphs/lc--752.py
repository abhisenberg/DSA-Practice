class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        #1. Helper function to get next set of combination
        def nextcombs(curr):
            nextlist = []
            for i in range(4):
                n = int(curr[i])
                
                n_up = (n + 1)%10
                n_down = (n + 9)%10

                n_up_str = curr[:i] + str(n_up) + curr[i+1:]
                n_down_str = curr[:i] + str(n_down) + curr[i+1:]

                nextlist.append(n_up_str)
                nextlist.append(n_down_str)
            return nextlist
        
        #2. Run BFS
        q = deque()
        seen = set()

        q.append("0000")
        for deadend in deadends:
            seen.add(deadend)
        
        lvl = 0
        while q:
            nicl = len(q)
            for _ in range(nicl):
                curr = q.popleft()

                if curr == target:
                    return lvl
                
                nexts = nextcombs(curr)
                for nextmove in nexts:
                    if nextmove not in seen:
                        q.append(nextmove)
                        seen.add(nextmove)

            lvl += 1

        return -1

from typing import List
from collections import deque

def minSplitMerge(arr1: List[int], arr2: List[int]) -> int:

    visited = set()
    q = deque()
    ans = float('inf')

    q.append((arr1, 0))
    visited.add(tuple(arr1))

    while q:
        arr, steps = q.popleft()

        if arr == arr2:
            ans = min(ans, steps)
            continue

        #generate all possible subarrays of this array
        for l in range(len(arr)):
            for r in range(l, len(arr)):
                #place them at all the possible remaining positions

                extracted = arr[l:r+1]
                remaining = arr[:l] + arr[r+1:]

                for i in range(len(remaining)+1):
                    newarr = remaining

                
                for k in range(l):
                    newarr = arr[:k] + arr[l:r+1] + arr[k:l] + arr[r+1:]
                    if tuple(newarr) not in visited:
                        visited.add(tuple(newarr))
                        q.append((newarr[:], steps+1))
                
                for k in range(r+2, len(arr)+1):
                    newarr = arr[:l] + arr[r+1:k] + arr[l:r+1] + arr[k:]
                    if tuple(newarr) not in visited:
                        visited.add(tuple(newarr))
                        q.append((newarr[:], steps+1))

    return int(ans)

# arr1 = [1,1,2,3,4,5]
# arr2 = [5,4,3,2,1,1]

arr1 = [3,1,2]
arr2 = [1,2,3]
print(minSplitMerge(arr1, arr2))
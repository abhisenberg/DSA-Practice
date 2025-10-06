from typing import List

def largestUniqueNumber(nums: List[int]) -> int:
    counts = [0]*1001
    for x in nums:
        counts[x] += 1

    print(counts)
    
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == 1:
            return i
    
    return -1

print(largestUniqueNumber([99]))
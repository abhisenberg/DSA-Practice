from typing import List

def findMaxAverage(nums: List[int], k: int) -> int:
    l, r, sum = 0, 0, 0
    
    while r < k:
        sum += nums[r]
        r += 1
    avg = sum / k
    
    mavg = avg
    
    while r < len(nums):
        avg = avg - (nums[l] - nums[r])/k
        mavg = max(mavg, avg)
        r += 1
        l += 1
    return mavg

avg = findMaxAverage([1,12,-5,-6,50,3], 4)
print(avg)
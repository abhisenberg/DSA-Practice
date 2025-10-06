from typing import List

def longestOnes(nums: List[int], k: int) -> int:        
    mlen, l, z = 0, 0, 0

    for r in range(len(nums)):
        if nums[r] == 0:
            z += 1

        while z > k:
            if nums[l] == 0:
                z -= 1
            l += 1

        mlen = max(mlen, r-l+1)

    return mlen

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))
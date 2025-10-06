from typing import List

def maximizeSweetness(nums: List[int], k: int) -> int:
    #0. Figure out the lowest and highest possible sum of any subarray that could be the maximized minimum of all 
    k += 1
    left = min(nums)    #The lowest possible would be the smallest element itself 
    right = sum(nums) // k #The highest possible could be the sum of all the elements 

    #1. Define a function where, given a number "limit", it can check whether the array can be divided in a way that the sum of each subarry is smaller than the given limit.
    def check(limit):
        subarrayCount = 0 #The count of the subarrays
        currentSubarraySum = 0 #Sum of the current subarray that is being iterated
        for n in nums:
            currentSubarraySum += n
            if currentSubarraySum >= limit: #If the curr sum goes over limit, begin new subarray
                subarrayCount += 1
                currentSubarraySum = 0  #New subarray sum starting from this num

        return subarrayCount >= k   #If the array can be divided into < k pieces which contain the largest subarray sum below limit, it can obviously be divided into k pieces as well

    #2. Run the binary search to find the minimum such number
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return right


nums = [1,2,3,4,5,6,7,8,9]
k = 5

# nums = [5,6,7,8,9,1,2,3,4]
# k = 8

# nums = [1,2,2,1,2,2,1,2,2]
# k = 2
print(maximizeSweetness(nums, k))
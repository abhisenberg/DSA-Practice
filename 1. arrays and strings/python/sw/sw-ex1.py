"""
Example 1: Given an array of positive integers nums and an integer k,
find the length of the longest subarray whose sum is less than or equal to k.
This is the problem we have been talking about above.
We will now formally solve it.
"""

def longestSubLessSum(arr, target):
    left = 0
    maxlen, currsum = 0, 0

    for right in range(len(arr)):
        currsum += arr[right]

        while currsum > target:
            currsum -= arr[left]
            left += 1
        
        maxlen = max(maxlen, right-left+1)

    print("Max len is: ", maxlen)
    return maxlen

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
longestSubLessSum(nums, k)
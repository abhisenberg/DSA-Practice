from typing import List
import time

"""
how to find the pivot of the rotated arrya?
in a normal sorted array, the middle element will always be less than the last element
but in a leftward rotated array,
    the middle element can be greater than the last element
        if the rotation is less than half the len of the array
    the middle element can be smaller than the last element
        if the rotation is more than half the len of the array

so, to find the pivot, we can compare the mid with the last element
if mid > the last element, the pivot (smallest number) lies in the right half
if mid <= the last element, the pivot (smallest number) lies in the left half

len : 7
rotated 0 times : 0 1 2 4 5 6 7
rotated 1 times : 1 2 4 5 6 7 0
rotated 2 times : 2 4 5 6 7 0 1
rotated 3 times : 4 5 6 7 0 1 2
rotated 4 times : 5 6 7 0 1 2 4
rotated 5 times : 6 7 0 1 2 4 5
rotated 6 times : 7 0 1 2 4 5 6
rotated 7 times : 0 1 2 4 5 6 7
"""

def find_pivot_index(arr: List[int]):
    l, r = 0, len(arr)-1
    while l < r:
        mid = (l+r)//2
        if arr[mid] > arr[r]:
            l = mid+1
        else:
            r = mid
    return l

def search(arr, target):
    n = len(arr)
    rotate_arr(arr, 3)

    """
    [0, pivot-1] is one sorted half
    [pivot, n-1] is the other one
    """

    pivot = find_pivot_index(arr)

    from bisect import bisect_left

    i = bisect_left(a=arr, x=target, lo=0, hi=pivot)
    if 0 <= i < n and arr[i] == target:
        return i
    
    i = bisect_left(a=arr, x=target, lo=pivot, hi=n)
    if 0 <= i < n and arr[i] == target:
        return i
    else:
        return -1


arr = [0, 1, 2, 4, 5, 6, 7]

def rotate_arr(arr: List[int], k: int):
    n = len(arr)
    
    def rev_arr(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    rev_arr(0, n-1)
    rev_arr(0, n-k-1)
    rev_arr(n-k, n-1)
 
if __name__ == "__main__":
    target=3
    print(search(arr, target))


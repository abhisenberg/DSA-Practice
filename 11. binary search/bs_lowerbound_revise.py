import bisect

def simpleBS(arr, target):
    l, r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
        
    return l

def lower_bound(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

#Case 1: Simple case, target element is present somewhere in the array
arr = [1,1,2,2,2,3,3,4,5,7]

print("Case 1: Simple case, target element is present somewhere in the array")
target = 5
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))

#Case 2: Simple case, target element is present at the left edge
arr = [1,1,2,2,2,3,3,4,5,7]

print("Case 2: Simple case, target element is present at the left edge")
target = 1
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))

#Case 3: Target element is not present in the array and is smaller than all
arr = [1,1,2,2,2,3,3,4,5,7]

print("Case 3: Target element is not present in the array and is smaller than all")
target = -1
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))

#Case 4: Target element is not present in the array, is smaller than all and has only one element in arry
arr = [1]

print("Case 4: Target element is not present in the array, is smaller than all and has only one element in arry")
target = 0
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))


#Case 5: Target element is not present in the array, is smaller than all and has only one element in arry
arr = []

print("Case 5: Array is empty")
target = 0
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))

#Case 6: Target element is not present in the array and is larger than all
arr = [1,1,2,2,2,3,3,4,5,7]

print("Case 6: Target element is not present in the array and is larger than all")
target = 8
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))

#Case 7: Target element is not present in the array, is smaller than all and has only one element in arry
arr = [1]

print("Case 7: Target element is not present in the array, is larger than all and has only one element in arry")
target = 2
print(bisect.bisect_left(arr, target))
print(lower_bound(arr, target))
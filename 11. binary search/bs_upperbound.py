def upperbound_bs(arr, target):
    left, right = 0, len(arr)   #Notice that 'right' is not len(arr)-1
    
    while left < right: #Notice that there is no equailty i.e. it is not <=
        mid = (left + right) // 2
        if target < arr[mid]:  #⚠️ Notice, no equality check here, this is crucial and the only difference between upper and lower bound
            right = mid #Notice that 'right = mid', not 'mid - 1'
        else:
            left = mid + 1
    return left

arr1 = [1,1,2,2,2,3,4,5,6,6,7]
target = 2
print(upperbound_bs(arr1, target))  #Index = 5 is returned, which is, rightmomst '2' = 4 + 1 = 5

arr1 = [1,1,2,2,2,4,5,6,6,7]
target = 3
print(upperbound_bs(arr1, target))  #Index = 5 is returned, since '3' should be inserted at index = 5, after all the 2s.

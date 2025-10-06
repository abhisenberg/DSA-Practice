"""
Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""

def combineSorted(list1, list2):
    result = []
    
    #1. Run both pointers till one runs out
    i, j = 0, 0
    m, n = len(list1), len(list2)
    while i < m and j < n:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    #2. Put elements of list1 if list2 has run out
    while i < m:
        result.append(list1[i])
        i += 1

    #3. Put elements of list2 if list1 has run out
    while j < n:
        result.append(list2[j])
        j += 1

    print(result)
    return result

a = [1,4,7,20]
b = [3,5,6]
combineSorted(a, b)
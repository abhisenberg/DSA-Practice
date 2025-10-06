from typing import List

def maximumSum(arr: List[int]) -> int:
    hm = {}
    ms = 0

    for x in arr:

        #Create digit sum
        digsum = 0
        temp = x
        while temp:
            digsum += temp % 10
            temp = temp // 10

        print("For ",x," , digsum = ", digsum)

        if digsum in hm:
            ms = max(ms, x + hm[digsum])
            hm[digsum] = max(x, hm[digsum])
        else:
            hm[digsum] = x

    return ms

print(maximumSum([18,43,36,13,7]))
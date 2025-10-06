def splitArray(arr):
        n = len(arr)

        #prefix sum
        sums = [0]*n
        sums[0] = arr[0]
        for k in range(1, n):
            sums[k] = sums[k-1] + arr[k]
        
        canInc, canDec = [False]*n, [False]*n
        canInc[0] = True
        canDec[n-1] = True

        #increasng
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                canInc[i] = True
            else:
                break

        #decreasing
        for i in range(n-2,0,-1):
            if arr[i] > arr[i+1]:
                canDec[i] = True
            else:
                break

        print(canInc)
        print(canDec)

        ans = float('inf')
        for i in range(n-1):
            if canInc[i] and canDec[i+1]:
                left = sums[i]
                right = sums[-1] - sums[i+1] + arr[i+1]
                ans = min(ans, abs(right-left))

        return -1 if ans == float('inf') else ans

print(splitArray([4,3]))
print(splitArray([1,3,2]))
print(splitArray([1,2,4,3]))
print(splitArray([3,1,2]))
print(splitArray([2,2]))
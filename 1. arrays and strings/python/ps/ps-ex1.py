
def solveQueries(nums, queries, limit):
    prefixSum = [nums[0]]
    for i in range(1, len(nums)):
        prefixSum.append(nums[i] + prefixSum[-1])
    
    ans = []
    for q in queries:
        qsum = prefixSum[q[1]] - prefixSum[q[0]] + nums[q[0]]
        ans.append((qsum < limit))

    print(ans)    
    return ans

nums = [1,6,3,2,7,2]
queries = [[0,3], [2,5], [2,4]]
limit = 13
solveQueries(nums, queries, limit)
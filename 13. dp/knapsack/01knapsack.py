def solveKnapsack_topdown(profits, weights, capacity):
    hm = {}
    n = len(profits)
    
    def dp(i, cap):
        if i == n or cap == 0:
            return 0
        
        if (i, cap) in hm:
            return hm[(i, cap)]
            
        ans = dp(i+1, cap)  # skip case
        if weights[i] <= cap:
            ans = max(ans, profits[i] + dp(i+1, cap - weights[i]))
        
        hm[(i, cap)] = ans
        return ans
    
    return dp(0, capacity)

def solveKnapsack_bottomup(profits, weights, capacity):
    n = len(profits)
    dp = [ [0]*(capacity+1) for _ in range(n+1) ]   #we do +1 to cover the base cases

    """
    items = 0 means no item available
    items = 1 means 1 item available, i=0
    items = 2 means 2 items available, i=0,1
    etc
    """
    for items in range(1, n+1):
        for cap in range(capacity+1):
            currItemIndex = items-1
            currItemWeight = weights[currItemIndex]
            currItemprofit = profits[currItemIndex]

            #skip case, we don't choose the current item
            dp[items][cap] = dp[items-1][cap]

            if currItemWeight <= cap:
                dp[items][cap] = max(dp[items][cap], currItemprofit + dp[items-1][cap-currItemWeight])
    
    return dp[n][capacity]

def solveKnapsack_bottomup_optimized(profits, weights, capacity):
    n = len(profits)
    dp = [0] * (capacity+1)   #we do +1 to cover the base cases

    """
    items = 0 means no item available
    items = 1 means 1 item available, i=0
    items = 2 means 2 items available, i=0,1
    etc
    """
    for currItemIndex in range(n):
        for cap in range(capacity, -1, -1):   #if we move 
            currItemWeight = weights[currItemIndex]
            currItemprofit = profits[currItemIndex]

            if currItemWeight <= cap:
                dp[cap] = max(dp[cap], currItemprofit + dp[cap-currItemWeight])
    return dp[capacity]

profits = [4,5,3,7]
weights = [2,3,1,4]
capacity = 5

ans = solveKnapsack_bottomup_optimized(profits, weights, capacity)
print(ans)
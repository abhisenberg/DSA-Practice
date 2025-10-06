
"""
nth = (n-1)th + (n-2)th
"""
def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)

"""
With memoization
"""
hm = {}
def fibm(n):
    if n == 0 or n == 1:
        return n
    
    if n in hm:
        return hm[n]

    hm[n] = fibm(n-1) + fibm(n-2)
    return hm[n]

"""
Bottom up
"""
def fibbu(n):
    ans = [0] * (n+1)
    ans[1] = 1
    for i in range(2, len(ans)):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[n]
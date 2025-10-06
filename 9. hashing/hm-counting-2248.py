from collections import defaultdict

def intmultarr(arr):
    hm = defaultdict(int)
    for i in range(len(arr)):
        for x in arr[i]:
            hm[x] += 1
        
    print(hm)
    
    ans = []
    for key in hm.keys():
        if hm[key] == len(arr):
            ans.append(key)
    
    ans.sort()
    return ans

print(intmultarr([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
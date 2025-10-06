from collections import defaultdict

def atmostdist(arr, k):
    l = 0
    ml, hmap = 0, defaultdict(int)
    
    for r in range(len(arr)):
        hmap[arr[r]] += 1

        while len(hmap) > k:
            hmap[arr[l]] -= 1
            if hmap[arr[l]] == 0:
                del hmap[arr[l]]
            l += 1
        
        ml = max(ml, r-l+1)
    
    print(ml)
    return ml


s = "eceba"
k = 2
atmostdist(s, k)

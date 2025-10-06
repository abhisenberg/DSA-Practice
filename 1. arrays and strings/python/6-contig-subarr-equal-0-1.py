from typing import List

def findMaxLength(arr: List[int]) -> int:
    count = [0,0]
    hm = {}
    
    #Creating hashmap containing counts of 0s and 1s
    for i in range(len(arr)):
        count[arr[i]] += 1
        hm[tuple(count)] = i


    #Iterating the hashmap and finding longest length
    ml = 0
    for k, v in hm.items():
        if k[0] > k[1]:
            d = k[0] - k[1]
            t = (d, 0)
            if t in hm:
                ml = max(ml, v-hm[t])
        else:
            d = k[1] - k[0]
            t = (0, d)
            if t in hm:
                ml = max(ml, v-hm[t])
    
    return ml

print(findMaxLength([0,1,0]))
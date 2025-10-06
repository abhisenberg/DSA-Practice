def unique(arr):
    hset = set(arr)
    for x in arr:
        if x+1 not in hset and x-1 not in hset:
            print(x)

arr = [1,2,4,6]
unique(arr)
from collections import defaultdict

def lc90(nums):

    n = len(nums)
    nums.sort()
    
    ans = []
    def swd(i, curr):
        #base case
        if i == n:
            ans.append(curr[:])
            return

        #case 1: add the element
        curr.append(nums[i])
        swd(i+1, curr)
        curr.pop()

        #case 2: skip the element -- we need to skip all the duplicates as well
        while i+1 < n and nums[i+1] == nums[i]:
            i += 1
        swd(i+1, curr)

    swd(0, [])
    return ans


nums = [1,2,2]
print(lc90(nums))
def permute(nums):
    ans = []

    def permu(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in curr:
                curr.append(nums[i])
                permu(curr)
                curr.pop()
    
    permu([])
    return ans

print(permute([1,2,3]))
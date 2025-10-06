from typing import List

class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subs(curr, start):
            ans.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                subs(curr, i+1)
                curr.pop()

        subs([], 0)
        return ans
    
sol = Solution()
print(sol.subsets([1,2,3]))
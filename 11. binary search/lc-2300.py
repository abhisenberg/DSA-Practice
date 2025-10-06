from typing import List

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:

    #0. FIrst we will sort the potions
    potions.sort()

    #1. Write binary search to find the leftmost insertion point of required potion strength
    def binSearch(target):
        l, r = 0, len(potions)-1
        while l < r:
            mid = (l + r) // 2
            if target <= potions[mid]:
                r = mid
            else:
                l = mid + 1
        print("For target {}, insertion point is {}".format(target, l))
        return l

    #2. For each spell, find required strength
    ans = []
    for s in spells:
        target = success/s
        print("For spell {}, target is {}".format(s, target))
        ans.append(len(potions)-binSearch(target))
    return ans

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

ans = successfulPairs(spells, potions, success)
print(ans)
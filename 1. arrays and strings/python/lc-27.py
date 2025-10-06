from typing import List

def removeElement(arr: List[int], val: int) -> int:
    count = 0
    while True:
        try:
            arr.remove(val)
            count += 1
        except ValueError:
            return count

    return count

a = [0,1,2,2,3,0,4,2]
b = 2
print(removeElement(a, b))
print(a)
import random

def main():
    n = random.randint(7,12)    #create a random size of the array
    arr = []
    for _ in range(n):
        arr.append(random.randint(1, 50))   #fill it with random elements

    st = SegTree(0, n-1, arr)
    
    for _ in range(100):
        choice = random.choice([True, False])
        if choice:      #do a range query
            l = random.randint(0,n-2)
            r = random.randint(l+1,n-1)

            rs = st.rangeSum(l,r)
            actualsum = sum(arr[l:r+1])

            print(f"Query: [{l},{r}] | actual = {actualsum} | rangesum = {rs} ")

            assert actualsum == rs

        else:           #update an element
            pos = random.randint(0, n-1)
            newele = random.randint(1, 50)
            arr[pos] = newele

            print(f"Update: pos = {pos} | new value = {newele}")

            st.pointUpdate(pos, newele)

    print("All tests passed! ✅")


def main2():
    arr = [4,2,6,1,8,3]

    st = SegTree(0, len(arr)-1, arr)
    print(st)
    l,r = 2,4

    rs = st.rangeSum(l,r)
    actualsum = sum(arr[l:r+1])

    print(f"found sum: {rs}, actual sum: {actualsum}")

class SegTree:
    """
    leftIndx, rightIndx:
        defines the range of the current segtree
    sum:
        defines the range sum of the current segtree
    leftChild, rightChild:
        the lefthalf and righthalf child of the current segtree
    """

    def __init__(self, leftIndx, rightIndx, arr):
        self.leftIndx = leftIndx
        self.rightIndx = rightIndx
        self.arr = arr

        if leftIndx == rightIndx:
            self.sum = arr[leftIndx]
        else:
            mid = (leftIndx+rightIndx) // 2
            self.leftChild = SegTree(leftIndx, mid, arr)
            self.rightChild = SegTree(mid+1, rightIndx, arr)
        
        self.recalculateSum()
            
    def recalculateSum(self):
        if self.leftIndx == self.rightIndx:
            self.sum = self.arr[self.leftIndx]
        else:
            self.sum = self.leftChild.sum + self.rightChild.sum

    def pointUpdate(self, pos, ele):
        if self.leftIndx == self.rightIndx and self.leftIndx == pos:
            self.sum = ele
            return
        
        if pos <= self.leftChild.rightIndx:
            self.leftChild.pointUpdate(pos, ele)
        else:
            self.rightChild.pointUpdate(pos, ele)
        
        self.recalculateSum()
        
    def rangeSum(self, l, r):
        #case 1: current range is outside of query
        if r < self.leftIndx or l > self.rightIndx:
            return 0

        #case 2: current range is completely covered under query
        if self.leftIndx >= l and self.rightIndx <= r:
            return self.sum
        
        #case 3: we don't know
        return self.leftChild.rangeSum(l,r) + self.rightChild.rangeSum(l,r)

main()

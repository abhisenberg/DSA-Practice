"""
This implementation of segtree has lazy propogation for range updates
"""

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
        self.lazy = 0       #keep the lazy data

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
        self.pushDown()

        if self.leftIndx == self.rightIndx and self.leftIndx == pos:
            self.sum = ele
            return
        
        if pos <= self.leftChild.rightIndx:
            self.leftChild.pointUpdate(pos, ele)
        else:
            self.rightChild.pointUpdate(pos, ele)
        
        self.recalculateSum()

    def rangeSum(self, l, r):
        self.pushDown()

        #case 1: current range is outside of query
        if r < self.leftIndx or l > self.rightIndx:
            return 0

        #case 2: current range is completely covered under query
        if self.leftIndx >= l and self.rightIndx <= r:
            return self.sum
        
        #case 3: we don't know
        return self.leftChild.rangeSum(l,r) + self.rightChild.rangeSum(l,r)

    def pushDown(self):
        if self.lazy == 0:  #nothing remaining to be pushed down
            return
        
        if self.leftIndx != self.rightIndx:     #if not leaf, pass the lazy down, they will handle it later
            self.leftChild.lazy += self.lazy
            self.rightChildlazy += self.lazy

        #update the current sum
        rangeSize = self.rightIndx - self.leftIndx + 1
        self.sum += self.lazy * rangeSize
        self.lazy = 0

    def rangeUpdate(self, l, r, val):
        self.pushDown()

        if r < self.leftIndx or l > self.rightIndx:
            return
        
        if self.leftIndx >= l and self.rightIndx <= r:
            self.lazy = val
            self.pushDown()
            return
        
        self.leftChild.rangeUpdate(l,r,val)
        self.rightChild.rangeUpdate(l,r,val)

        self.leftChild.pushDown()
        self.rightChild.pushDown()
        self.recalculateSum()
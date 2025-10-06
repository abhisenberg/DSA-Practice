class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Basically, we have to keep finding the maximum and minimum of a 
        running window in an array as we go.
        
        Attribute to maximize: length of the subarray = j-i+1
        Constraint: max - min <= limit

        To find the running max and min of the array, we will use
        double-ended queues, and use
            - a monotonically decreasing queue to find the max
            - a monotonically increasing queue to find the min
        """

        qmax = collections.deque()  #This Q holds max element at pos 0
        qmin = collections.deque()  #This Q holds min element at pos 0

        maxLen = 0
        left = right = 0

        #The ele will remove all ele smaller than itself in the qmax
        #And it will remove all ele larger than itself in the qmin
        for right in range(len(nums)):
            while qmax and nums[right] > qmax[-1]:
                qmax.pop()
            while qmin and nums[right] < qmin[-1]:
                qmin.pop()

            qmax.append(nums[right])
            qmin.append(nums[right])

            #Maintaining the window property
            #qmax[0] is the max element, qmin[0] is the min element
            while qmax[0] - qmin[0] > limit:
                if qmax[0] == nums[left]:
                    qmax.popleft()
                if qmin[0] == nums[left]:
                    qmin.popleft()

                left += 1
            
            maxLen = max(right-left+1, maxLen)

        return maxLen
            


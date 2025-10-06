class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        
        #In the stack, we will insert the index of elements and refer to the
        #values through the original array
        stack = []  
        ans = [0]*len(arr)

        #Run the algo for the rest of the array
        for i in range(len(arr)):
            
            #Remove all the elements smaller or equal than this element
            #And store their answer, which is, their index - curren index
            while stack and arr[stack[-1]] < arr[i]:
                removedEle = stack.pop()
                ans[removedEle] = i - removedEle
            
            stack.append(i)

        return ans

"""
Any element from stack will only be popped when an element greater than itself 
comes into the stack. Hence, at all points when we remove an element, we will know
that the coming element is the "next greater element".

The stack that is created is a monotonically non-increasing stack. 
"""
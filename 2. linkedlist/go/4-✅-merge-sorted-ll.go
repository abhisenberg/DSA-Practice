package main

/*

https://leetcode.com/problems/merge-two-sorted-lists/description/

Solution:
https://www.youtube.com/watch?v=XIdigk956u0


*/

//Recursion: TODO
func mergeRecursion(h1 *ListNode, h2 *ListNode) *ListNode {

	if h1 == nil {
		return h2
	}

	if h2 == nil {
		return h1
	}

	retVal := &ListNode{}
	if h1.Val <= h2.Val {
		retVal = h1
		retVal.Next = mergeRecursion(h1.Next, h2)
	} else {
		retVal = h2
		retVal.Next = mergeRecursion(h1, h2.Next)
	}

	return retVal

}

//Iteration
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{0, nil}
	c3 := dummy

	c1, c2 := list1, list2

	for c1 != nil && c2 != nil {

		if c1.Val <= c2.Val {
			c3.Next = c1
			c1 = c1.Next
		} else {
			c3.Next = c2
			c2 = c2.Next
		}

		c3 = c3.Next
	}

	if c1 != nil {
		c3.Next = c1
	} else {
		c3.Next = c2
	}

	return dummy.Next
}

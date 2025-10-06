package main

/*
https://leetcode.com/problems/reverse-linked-list/description/
*/

//Using iteration
func reverseList(head *ListNode) *ListNode {
	var p *ListNode
	var c *ListNode
	c = head
	for c != nil {
		tempNext := c.Next
		c.Next = p
		p = c
		c = tempNext
	}

	return p
}

//Using Recursion
func reverse(c *ListNode, p *ListNode) *ListNode {
	if c == nil {
		return p
	}

	tempNext := c.Next
	c.Next = p
	p = c
	c = tempNext

	return reverse(c, p)
}

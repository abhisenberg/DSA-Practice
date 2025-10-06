package main

//https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

func deleteDuplicates82(head *ListNode) *ListNode {
	dummy := &ListNode{}
	l := dummy
	r := head

	for r != nil {

		for r.Next != nil && r.Val != r.Next.Val {
			l = r
			r = r.Next
		}

		if r.Next == nil {
			l.Next = r
			break
		}

		for r.Next != nil && r.Val == r.Next.Val {
			r = r.Next
		}

		if r.Next == nil {
			l.Next = nil
			break
		}

		l.Next = r.Next
		r = r.Next
	}

	return dummy.Next

}

func deleteDuplicates82_2(head *ListNode) *ListNode {
	dummy := &ListNode{0, head}
	l := dummy
	r := head

	for r != nil {
		if r.Next != nil && r.Val == r.Next.Val {
			for r.Next != nil && r.Val == r.Next.Val {
				r = r.Next
			}
			l.Next = r.Next
		} else {
			l = l.Next
		}
		r = r.Next
	}

	return dummy.Next

}

func deleteDuplicates81(head *ListNode) *ListNode {
	fo, lo := head, head
	for fo != nil {
		for lo != nil && fo.Val == lo.Val {
			lo = lo.Next
		}
		fo.Next = lo
		fo = lo
	}
	return head
}

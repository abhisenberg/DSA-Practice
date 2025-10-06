package main

//https://leetcode.com/problems/copy-list-with-random-pointer/

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {

	if head == nil {
		return nil
	}

	//Step 1: Create each node's copy and assign same random node as original list's nodes
	h1 := head
	for h1 != nil {
		copy := &Node{Val: h1.Val}
		copy.Random = h1.Random

		tn := h1.Next
		h1.Next = copy
		copy.Next = tn

		h1 = h1.Next.Next
	}

	//Step 2: Move the copy-node's random pointers one step ahead so that they point to the copy-nodes
	h2 := head.Next
	for h2 != nil {
		if h2.Random != nil {
			h2.Random = h2.Random.Next
		}
		if h2.Next == nil {
			break
		}
		h2 = h2.Next.Next
	}

	//Step 3: Un-weave the 2 lists
	on := head      //Original node
	cn := head.Next //Copy nodes
	newHead := cn
	for on != nil {
		on.Next = cn.Next
		if cn.Next != nil {
			cn.Next = cn.Next.Next
		}
		on = on.Next
		cn = cn.Next
	}

	return newHead
}

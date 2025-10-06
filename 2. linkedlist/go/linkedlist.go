package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type Linkedlist struct {
	head   *ListNode
	tail   *ListNode
	length int
}

func (l *Linkedlist) create(arr *[]int) {
	for _, val := range *arr {
		l.addAtLast(&ListNode{Val: val})
	}
}

func (l *Linkedlist) show() {
	curr := l.head
	for curr != nil {
		fmt.Print(curr.Val, " -> ")
		curr = curr.Next
	}
	fmt.Println("")
}

func (l *ListNode) show() {
	curr := l
	for curr != nil {
		fmt.Print(curr.Val, " -> ")
		curr = curr.Next
	}
	fmt.Println("")
}

func (l *Linkedlist) addAtFirst(n *ListNode) {
	n.Next = l.head
	l.head = n

	if l.tail == nil {
		l.tail = l.head
	}

	l.length++
}

func (l *Linkedlist) addAtLast(n *ListNode) {
	if l.tail != nil {
		l.tail.Next = n
	}

	l.tail = n

	if l.head == nil {
		l.head = l.tail
	}

	l.length++
}

func (l *Linkedlist) removeHead() {
	if l.head == nil {
		return
	}

	temp := l.head
	l.head = l.head.Next
	temp.Next = nil
	l.length--
}

func (l *Linkedlist) removeTail() {
	if l.head == nil {
		return
	}

	if l.head == l.tail {
		l.removeHead()
		return
	}

	curr := l.head
	for curr.Next != l.tail {
		curr = curr.Next
	}

	curr.Next = nil
	l.tail = curr
	l.length--
}

func (l *Linkedlist) removeAtIndex(target int) {
	if l.length <= target {
		return
	}

	if target == 0 {
		l.removeHead()
		return
	}

	if target == l.length-1 {
		l.removeTail()
		return
	}

	i := 0
	curr := l.head
	for i < target-1 {
		curr = curr.Next
		i++
	}

	temp := curr.Next
	curr.Next = curr.Next.Next
	temp.Next = nil
	l.length--
}

func (l *Linkedlist) addAtIndex(targetIndx int, targetValue int) {
	if targetIndx > l.length || targetIndx < 0 {
		return
	}

	newNode := &ListNode{Val: targetValue}

	if targetIndx == 0 {
		l.addAtFirst(newNode)
		return
	}

	if targetIndx == l.length {
		l.addAtLast(newNode)
		return
	}

	i := 0
	curr := l.head
	for i < targetIndx-1 {
		curr = curr.Next
		i++
	}

	newNode.Next = curr.Next
	curr.Next = newNode
	l.length++

}

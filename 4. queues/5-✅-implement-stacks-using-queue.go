package main

//https://leetcode.com/problems/implement-stack-using-queues/

/*
We will be using one queue to mimic a stack.
*/

type MyStack struct {
	queue Queue
}

func ConstructorA() MyStack {
	return MyStack{
		queue: Queue{},
	}
}

func (this *MyStack) Push(x int) {
	this.queue.enqueue(x)
	currSize := len(this.queue)
	for i := 0; i < currSize-1; i++ {
		ele := this.queue.dequeue()
		this.queue.enqueue(ele)
	}
}

func (this *MyStack) Pop() int {
	return this.queue.dequeue().(int)
}

func (this *MyStack) Top() int {
	return this.queue.peek().(int)
}

func (this *MyStack) Empty() bool {
	return this.queue.isEmpty()
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */

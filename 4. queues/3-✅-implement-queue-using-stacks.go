type MyQueue struct {
	stack1 *Stack
	stack2 *Stack
}

func Constructor() MyQueue {
	return MyQueue{
		stack1: new(Stack),
		stack2: new(Stack),
	}
}

func (this *MyQueue) Push(x int) {
	this.stack1.Push(x)
}

func (this *MyQueue) Pop() int {
	if this.stack2.isEmpty() {
		for !this.stack1.isEmpty() {
			this.stack2.Push(this.stack1.Pop())
		}
	}

	if !this.stack2.isEmpty() {
		return this.stack2.Pop().(int)
	}

	return 0
}

func (this *MyQueue) Peek() int {
	if this.stack2.isEmpty() {
		for !this.stack1.isEmpty() {
			this.stack2.Push(this.stack1.Pop())
		}
	}

	if !this.stack2.isEmpty() {
		return this.stack2.Peek().(int)
	}

	return 0
}

func (this *MyQueue) Empty() bool {
	return this.stack1.isEmpty() && this.stack2.isEmpty()
}

type Stack []interface{}

func (s *Stack) Push(item interface{}) {
	*s = append(*s, item)
}

func (s *Stack) Pop() interface{} {
	if len(*s) == 0 {
		return nil
	}

	indexToRemove := len(*s) - 1
	item := (*s)[indexToRemove]
	*s = (*s)[:indexToRemove]
	return item
}

func (s *Stack) Peek() interface{} {
	if len(*s) == 0 {
		return nil
	}

	return (*s)[len(*s)-1]
}

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

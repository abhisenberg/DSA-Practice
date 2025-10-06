package main

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

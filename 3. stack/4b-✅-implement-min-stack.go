package main

//https://leetcode.com/problems/min-stack/

type MinStackOptimal struct {
	stack []int
	min   int
}

func ConstructorMSO() MinStackOptimal {
	return MinStackOptimal{
		stack: []int{},
		min:   -1,
	}
}

func (s *MinStackOptimal) Push(val int) {
	if len(s.stack) == 0 {
		s.min = val
	}

	if val >= s.min {
		s.stack = append(s.stack, val)
	} else {
		valToPush := 2*val - s.min
		s.stack = append(s.stack, valToPush)
	}
}

func (s *MinStackOptimal) Pop() {
	if len(s.stack) == 0 {
		return
	}

	topVal := s.stack[len(s.stack)-1]  //Get the top value
	s.stack = s.stack[:len(s.stack)-1] //Delete the top value

	if topVal < s.min {
		s.min = 2*topVal - s.min //If this element was the min element till that point in stack, retract the min
	}
}

func (s *MinStackOptimal) Top() int {
	if len(s.stack) == 0 {
		return -1
	}

	topVal := s.stack[len(s.stack)-1] //Get the top value

	if topVal >= s.min {
		return topVal
	} else {
		return s.min
	}
}

func (s *MinStackOptimal) GetMin() int {
	return s.min
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

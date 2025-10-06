package main

//https://leetcode.com/problems/next-greater-element-i/

func nextGreaterElement(b []int, a []int) []int {
	var ans []int
	var stack []int
	ansm := make(map[int]int)

	for i := len(a) - 1; i >= 0; i-- {

		for len(stack) > 0 && (stack[len(stack)-1] < a[i]) { //While the top element of the stack is smaller than the current element
			stack = stack[:len(stack)-1]
		}

		if len(stack) == 0 {
			stack = append(stack, a[i])
			ansm[a[i]] = -1
			continue
		}

		ansm[a[i]] = stack[len(stack)-1]
		stack = append(stack, a[i])
	}

	for i := 0; i < len(b); i++ {
		ans = append(ans, ansm[b[i]])
	}

	return ans
}

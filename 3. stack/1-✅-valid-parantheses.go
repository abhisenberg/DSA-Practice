package main

//https://leetcode.com/problems/valid-parentheses/

func isValid(s string) bool {
	var stack [10000]rune
	top := -1

	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '(' || c == '[' || c == '{' {
			top++
			stack[top] = rune(c)
		} else if top != -1 {
			if (c == ')' && stack[top] == '(') || (c == ']' && stack[top] == '[') || (c == '}' && stack[top] == '{') {
				top--
			} else {
				return false
			}
		} else {
			return false
		}
	}

	return top == -1
}

/*
This solution uses an array of fixed size and an index pointer "top".
This could also be done using a list and using functions like append and pop.
This one is cleaner and faster.
*/

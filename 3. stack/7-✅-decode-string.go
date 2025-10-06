package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

//https://leetcode.com/problems/decode-string/

func decodeString(s string) string {
	var stack []interface{}

	for i := 0; i < len(s); i++ {
		// fmt.Printf("C: %v, digit: %d, digErr: %s\n", s[i], digit, digerr)

		if unicode.IsDigit(rune(s[i])) { //current character is a digit
			currNumberStr := ""
			for i < len(s) && unicode.IsDigit(rune(s[i])) {
				currNumberStr += string(s[i])
				i++
			}

			currNumber, _ := strconv.Atoi(currNumberStr)
			stack = append(stack, currNumber)
			// fmt.Println("#1: Inserted ", currNumber, " in stack. Stack is ", stack)
		}
		if s[i] != ']' && s[i] != '[' { //current character is an alphabet
			stack = append(stack, string(s[i]))
			// fmt.Println("#2: Inserted ", string(s[i]), " in stack. Stack is ", stack)
		} else if s[i] == ']' {
			x, r := "", 0
			for !isTopADigit(&stack) {
				x = stack[len(stack)-1].(string) + x
				stack = stack[:len(stack)-1]
			}
			if isTopADigit(&stack) {
				r = stack[len(stack)-1].(int)
				stack = stack[:len(stack)-1]
			}

			x = strings.Repeat(x, r)
			stack = append(stack, x)
		}
	}

	fmt.Println("Stack: ", stack)

	ans := ""
	for len(stack) > 0 {
		ans = stack[len(stack)-1].(string) + ans
		stack = stack[:len(stack)-1]
	}
	return ans
}

func isTopADigit(stack *[]interface{}) bool {
	switch (*stack)[len(*stack)-1].(type) {
	case int:
		return true
	default:
		return false
	}
}

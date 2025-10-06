package main

import (
	"fmt"
	"strconv"
)

//https://leetcode.com/problems/evaluate-reverse-polish-notation/

func evalRPN(tokens []string) int {
	var nums [10000]int
	topIndex := -1

	for i := 0; i < len(tokens); i++ {
		c := tokens[i]
		if c == "+" || c == "-" || c == "*" || c == "/" {
			a := nums[topIndex]
			topIndex--
			b := nums[topIndex]
			topIndex--

			res := operate(a, b, c)
			topIndex++
			nums[topIndex] = res

		} else {
			ci, _ := strconv.Atoi(c)
			topIndex++
			nums[topIndex] = ci
		}
	}

	if topIndex != 0 {
		fmt.Println("!!")
		return -1
	}

	return nums[topIndex]
}

func operate(a int, b int, c string) int {
	switch c {
	case "+":
		return a + b
	case "-":
		return b - a
	case "*":
		return b * a
	case "/":
		return b / a
	}
	return 0
}

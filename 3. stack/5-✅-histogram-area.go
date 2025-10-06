package main

import "fmt"

//https://leetcode.com/problems/largest-rectangle-in-histogram/
/*
Uses the concept of "next smaller element" and "previous smaller element"
*/

func largestRectangleArea(heights []int) int {
	nse := createNse(heights)
	pse := createPse(heights)

	fmt.Println(nse)
	fmt.Println(pse)

	maxArea := 0
	for i := 0; i < len(heights); i++ {
		area := (nse[i] - pse[i] - 1) * heights[i]
		maxArea = max(maxArea, area)
	}

	return maxArea

}

type ele struct {
	val   int
	index int
}

func createNse(a []int) []int {
	n := len(a)

	nse := make([]int, n)
	var stack []ele

	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && a[i] <= stack[len(stack)-1].val {
			stack = stack[:len(stack)-1]
		}

		if len(stack) == 0 {
			nse[i] = n
			stack = append(stack, ele{a[i], i})
		}

		if a[i] > (stack[len(stack)-1]).val {
			nse[i] = stack[len(stack)-1].index
			stack = append(stack, ele{a[i], i})
		}
	}

	return nse
}

func createPse(a []int) []int {
	n := len(a)

	nse := make([]int, n)
	var stack []ele

	for i := 0; i < n; i++ {
		for len(stack) > 0 && a[i] <= (stack[len(stack)-1]).val {
			stack = stack[:len(stack)-1]
		}

		if len(stack) == 0 {
			nse[i] = -1
			stack = append(stack, ele{a[i], i})
		}

		if a[i] > (stack[len(stack)-1]).val {
			nse[i] = stack[len(stack)-1].index
			stack = append(stack, ele{a[i], i})
		}
	}

	return nse
}

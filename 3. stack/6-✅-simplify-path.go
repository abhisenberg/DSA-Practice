package main

import (
	"fmt"
	"strings"
)

//https://leetcode.com/problems/simplify-path/

func canonicalPath(path string) {
	var stack []string
	dirs := strings.Split(path, "/")

	for _, dir := range dirs {
		switch dir {
		case "", ".":
			continue
		case "..":
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		default:
			stack = append(stack, dir)
		}
	}

	ans := ""
	for i := len(stack) - 1; i >= 0; i-- {
		ans = "/" + stack[i] + ans
	}

	if ans == "" {
		ans = "/"
	}

	fmt.Println(ans)
}

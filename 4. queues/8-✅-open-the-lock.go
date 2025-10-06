package main

import "fmt"

//https://leetcode.com/problems/open-the-lock/

func openLock(deadends []string, target string) int {
	//Create a visited map, it is also going to be used as a deadend
	visited := make(map[string]struct{})

	//Fill the deadends into visited so that they are never taken
	for _, de := range deadends {
		visited[de] = struct{}{}
	}

	//Create a queue
	queue := Queue{}
	queue.enqueue("0000")

	//In that queue, keep a count of the "moves done till now" (or depth of the tries made)
	moves := 0
	for !queue.isEmpty() {
		levSize := len(queue)
		for levSize != 0 {

			currCode := queue.dequeue().(string)
			fmt.Println("Curr code: ", currCode)
			if currCode == target {
				return moves
			}

			nextCodes := nextCodes(currCode)
			for _, code := range nextCodes {
				_, exists := visited[code]
				if !exists {
					queue.enqueue(code)
					visited[code] = struct{}{}
				}
			}

			levSize--
		}
		moves++
	}

	return -1
}

func nextCodes(code string) []string {
	ans := []string{}

	for i := 0; i < len(code); i++ {
		a := code[:i] + fmt.Sprint((int(code[i]-'0')+1)%10) + code[i+1:]
		b := code[:i] + fmt.Sprint((int(code[i]-'0')+9)%10) + code[i+1:]
		ans = append(ans, a)
		ans = append(ans, b)
	}

	return ans
}

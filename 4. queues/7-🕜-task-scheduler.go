package main

import "fmt"

//https://leetcode.com/problems/task-scheduler/

func leastInterval(tasks []byte, n int) int {
	remTasks := new([26]ele)
	totalTasks := len(tasks)

	for _, x := range tasks {
		remTasks[x-'A'].rem++
		remTasks[x-'A'].prevInterval = -101
	}

	fmt.Println(remTasks)

	i := 0
	for totalTasks != 0 {
		task := -1

		for ind, _ := range remTasks {
			x := &remTasks[ind]
			if x.rem > 0 && (i-x.prevInterval > n) {
				totalTasks--
				x.rem--
				x.prevInterval = i
				task = ind
				break
			}
		}
		fmt.Println("i: ", i, ", task: ", task)
		i++
	}

	return i
}

type ele struct {
	rem          int
	prevInterval int
}

func test() {
	arr := new([1]ele)
	arr[0].rem++
	arr[0].prevInterval++

	for ind, _ := range arr {

		arr[ind].rem--
		arr[ind].prevInterval--
	}
}

/*
for ind, x := range remTasks {
			if x.rem > 0 && (i-x.prevInterval > n) {
				fmt.Println("")
				totalTasks--
				x.rem--
				x.prevInterval = i
				task = ind
				fmt.Println(remTasks)
				break
			}
		}
*/
